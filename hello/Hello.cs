using System;
using System.Collections;
using System.Windows.Forms;

/*public class Hello{

	static void Main(string[] args){
		double [][] ar = new double[1][];
		double n = 2.5*10%10;
		ar[0] = new double [1];
		ar[0][0] = n;
		//Console.WriteLine(ar[0][0].ToString());
		//double[,] data = new double[2,3];
		//Console.WriteLine(data.GetLength(0));
		//Console.WriteLine(data.GetLength(1));
		//Console.Read();
		Form form = new Form();
		form.ShowDialog();

	}
}*/

using System.Windows;

namespace SDKSample
{
    public partial class AWindow : Window
    {
        public AWindow()
        {
            // InitializeComponent call is required to merge the UI
            // that is defined in markup with this class, including  
            // setting properties and registering event handlers
            InitializeComponent();
        }

        void button_Click(object sender, RoutedEventArgs e)
        {
            // Show message box when button is clicked.
            MessageBox.Show("Hello, Windows Presentation Foundation!");
        }
    }
}