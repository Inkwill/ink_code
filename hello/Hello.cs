using System;
using System.Collections;

public class Hello{

	static void Main(string[] args){
		double [][] ar = new double[1][];
		double n = 2.5*10%10;
		ar[0] = new double [1];
		ar[0][0] = n;
		Console.WriteLine(ar[0][0].ToString());
		/*double[,] data = new double[2,3];
		Console.WriteLine(data.GetLength(0));
		Console.WriteLine(data.GetLength(1));*/
		Console.Read();
	}
}

