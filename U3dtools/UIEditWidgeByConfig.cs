/*************************************
 *	功 能: 通过配置修改控件属性
 *	作 者: 
 *	创 建: 
 *	修 改:
*************************************/

using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Data;
using UnityEditor;
using UnityEngine;

namespace ProjectS.Edi
{
    public class UIEditWidgeByConfig : EditorWindow
    {
        private const string UIFormPath = "Assets/GameMain/UI/Forms";
        private List<string> configList = new List<string>();
        private string currentProcess= "";
        private Vector2 _scrollPos;
        private DataTable labelConfig;
        private List<GameObject> uiObjList = new List<GameObject>();
        private List<string> objValueList = new List<string>();
        private List<bool> toggleList = new List<bool>();
        private List<bool> uiTogList = new List<bool>();

        [MenuItem("Project-S/界面工具/快捷工具 &r")]
        public static void ShowWindow()
        {
            UIEditWidgeByConfig window = GetWindow(typeof(UIEditWidgeByConfig)) as UIEditWidgeByConfig;
            window.titleContent = new GUIContent("界面快捷工具");
            window.position = new Rect(400, 150, 900, 700);
            window.Show();
        }

        void ClearContent(){

            uiObjList.Clear();
            objValueList.Clear();
            configList.Clear();
            toggleList.Clear();
            uiTogList.Clear();
            currentProcess = string.Join(" ",CurrentSelectedNames());
        }

        private void OnGUI()
        {
            GUIStyle style = new GUIStyle();
            style.fontSize = 12;

//按钮区域
            if (GUILayout.Button("批量处理Lable"))
            {
                ClearContent();
                ProcessLabelConfig();
                if(uiObjList.Count>0){
                    currentProcess = "批量处理Lable";
                }
                else {
                    currentProcess = "未找到可处理的Lable.---" + string.Join(" ",CurrentSelectedNames());
                }
            }
            if (GUILayout.Button("规整坐标")){

                ClearContent();
                RegularPosition();
                 if(uiObjList.Count>0){
                    currentProcess = "规整坐标";
                }
                else {
                    currentProcess = "未找到需要规整的坐标.---" + string.Join(" ",CurrentSelectedNames());
                }
            }
//提示区域
            if (configList.Count > 0){
                for (int i = 0; i < configList.Count; i++)
                    {
                        GUILayout.Label(string.Format("<color=white><b>     {0}</b></color>", configList[i]), style, GUILayout.Width(190f));
                    }
            }
//修改内容区域
            _scrollPos = GUILayout.BeginScrollView(_scrollPos);
            for (int i = 0; i < uiObjList.Count; i++)
            {
                GUILayout.BeginHorizontal();
                //GUILayout.Toggle(true, "", GUILayout.MinWidth(1f));
                EditorGUILayout.ObjectField("", uiObjList[i], typeof(UnityEngine.Object), true, GUILayout.Width(300));
                if(objValueList.Count > i){
                    if(toggleList.Count > i && uiTogList.Count > i){
                        if(toggleList[i] != GUILayout.Toggle(uiTogList[i],"")){
                           toggleList[i] = !toggleList[i];
                           uiTogList[i] = !uiTogList[i];
                        }
                    }
                    string color = toggleList[i] ? "<color=green>     {0}</color>" : "<color=white>     {0}</color>";
                    GUILayout.Label(string.Format(color, objValueList[i]), style, GUILayout.Width(190f));
                    //GUILayout.Label(string.Format("<color=green>     {0}</color>", objValueList[i]), style, GUILayout.Width(190f));
                }
                GUILayout.EndHorizontal();
            }
            GUILayout.EndScrollView();
            if (uiObjList.Count > 0){

                if (GUILayout.Button("批量修改")){

                    if(currentProcess == "批量处理Lable"){
                        ProcessLabel();
                    }
                    else if(currentProcess == "规整坐标"){
                        ProcessPositon();
                    }
                    //ClearContent();
                    //ProcessLabelConfig();
                }
            }
//提示区域  
            GUILayout.FlexibleSpace();
            GUILayout.Label(string.Format("<color=white>     {0}</color>", currentProcess), style, GUILayout.Width(190f));
        }

//读取配置文件
         static DataTable txtTable(string filePath) {

            string[] result = File.ReadAllLines(filePath);
            string[] columnsName = result[0].Split('\t');

            DataTable dt = new DataTable();
            foreach (string key in columnsName) 
            {
                dt.Columns.Add(key, typeof(string));
            }
           
            for (int i =1;i<result.Length;i++) 
            {
               string[] strs = result[i].Split('\t');
               DataRow dr = dt.NewRow();
               for (int j=0; j< strs.Length; j++) 
               {
                  dr[j] = strs[j]; 
               }
               dt.Rows.Add(dr);
            }

            return dt;
        }

        string[] GetColumnName(DataTable dt) {

            if(dt.Columns.Count == 0){
                return null;
            }
           int columnNum = dt.Columns.Count;
           string[] columnNames = new string[columnNum];
           for(int i = 0; i < dt.Columns.Count; i++){
                columnNames[i] = dt.Columns[i].ColumnName;
           }
           return columnNames;
        }

        List<string> CurrentSelectedNames(){

            List<string> objNames = new List<string>();
            objNames.Add(String.Format("selected({0}):",Selection.gameObjects.Length));
            if(Selection.gameObjects != null){
                foreach (GameObject obj in Selection.gameObjects) 
                {
                   objNames.Add(obj.name); 
                }
            }
            return objNames;
        }

        void RegularPosition(){

            foreach (GameObject obj in Selection.gameObjects) 
            {
                Transform[] trans = obj.GetComponentsInChildren<Transform>();
                foreach (Transform t in trans) 
                {
                    if(!IsRegularPosition(t)){

                        uiObjList.Add(t.gameObject);
                        objValueList.Add(t.localPosition.ToString());
                        toggleList.Add(true);
                        uiTogList.Add(true);
                    }
                }
            }
        }

        bool IsRegularPosition(Transform t){

            float[] pos = {t.localPosition.x,t.localPosition.y,t.localPosition.z};
            foreach (float n in pos) 
            {
                if(Math.Abs(n*10%10) >1){
                   //Debug.Log(string.Format("{0}-{1}",n,n*10%10));
                    return false;
                }
            }
            return true;
        }

        void ProcessPositon(){
            for (int i= uiObjList.Count -1; i>= 0;i--) 
            {
                if(!toggleList[i])
                    break;
                Vector3 pos = uiObjList[i].GetComponent<Transform>().localPosition;
                pos.x = (float)Math.Round(pos.x,MidpointRounding.AwayFromZero);
                pos.y = (float)Math.Round(pos.y,MidpointRounding.AwayFromZero);
                pos.z = (float)Math.Round(pos.z,MidpointRounding.AwayFromZero);
                uiObjList[i].GetComponent<Transform>().localPosition = pos;
                RemoveElement(i);
            }
        }

        void ProcessLabelConfig(){

            labelConfig = txtTable(Application.dataPath +"/GameMain/UI/tools/LabelConfig.txt");
            configList.Add(string.Join("\t",GetColumnName(labelConfig)));
            foreach (DataRow row in labelConfig.Select(String.Format("{0} = '1'",GetColumnName(labelConfig)[0])))
            {
                configList.Add(string.Join("\t",row.ItemArray));
            }
            foreach (GameObject obj in Selection.gameObjects) {

                foreach (UILabel lb in obj.GetComponentsInChildren<UILabel>()) 
                {
                    if(IsConfigLabel(lb)){
                        uiObjList.Add(lb.gameObject);
                        toggleList.Add(true);
                        uiTogList.Add(true);
                    }
                }
            }
        }

        bool IsConfigLabel(UILabel lb){
            foreach (DataRow row in labelConfig.Rows) 
            {
                if(row["Key"].ToString() == "text"){
                    if(lb.text == row["Value"].ToString()){
                        objValueList.Add(String.Format("{0} : Set {1} to : {2}",row["Value"],row["setKey"],row["setValue"]));
                        return true;
                    }
                }
            }
            return false;
        }

        void ProcessLabel(){

            List<int> idList = new List<int>();
            for (int i = uiObjList.Count -1; i>= 0; i--) 
            {
                if(!toggleList[i])
                    break;
                string key = labelConfig.Rows[i]["setKey"].ToString();
                string value = labelConfig.Rows[i]["setValue"].ToString();
                if(key == "text"){
                    uiObjList[i].GetComponent<UILabel>().text = value;
                }
                else if(key == "color"){
                    Color newCol;
                    if(ColorUtility.TryParseHtmlString("#" + value, out newCol))
                        uiObjList[i].GetComponent<UILabel>().color = newCol;
                }
                RemoveElement(i);
            }
        }

        void RemoveElement(int i){

            uiObjList.RemoveAt(i);
            objValueList.RemoveAt(i);
            toggleList.RemoveAt(i);
            uiTogList.RemoveAt(i);
        }
    }
}
