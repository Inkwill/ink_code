/*************************************
 *	功 能: 切换物体显隐状态
 *	作 者: 
 *	创 建: 
 *	修 改:
*************************************/

using System.Collections.Generic;
using System.IO;
using UnityEditor;
using UnityEngine;

namespace ProjectS.Edi
{
    public class UISpriteOrTextureTools : EditorWindow
    {
         [MenuItem("Project-S/界面工具/切换物体显隐状态 &q")]
        public static void SetObjActive()
        {
            GameObject[] selectObjs = Selection.gameObjects;
            int objCtn = selectObjs.Length;
            for (int i = 0; i < objCtn; i++)
            {
                bool isAcitve = selectObjs[i].activeSelf;
                selectObjs[i].SetActive(!isAcitve);
            }
        }
    }
}
