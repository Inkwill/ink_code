namespace CSharpPrimer{

using System;
using System.IO;
using System.Collections;

class EntryPoint{

	public delegate void WriteFun();
	static ArrayList textArray = new ArrayList();

	public static void Main(string[] args){

		string fileName = "";
		WriteFun WriteTo = null; 

		if (args.Length == 0){
			Console.WriteLine("check_valid_file_type(option)");
			Console.Read();
		}

		foreach(string option in args){

			switch (option){

				case "-c":
					WriteTo = new WriteFun(writeToConsole);
					break;
				case "-f":
					WriteTo = new WriteFun(writeToFile);
					break;
				case "-h":
					display_usage();
					break;
				default:
					if(option.Length>4 && option.Substring(option.Length -4,4) == ".txt"){

						fileName = option;
					}
					break;
			}
		}
		if(WriteTo == null)
			WriteTo = new WriteFun(writeToConsole);
		if(fileName == ""){

			Console.WriteLine("A valid filename is required!");
			Console.Read();
		}
		else if(File.Exists(Directory.GetCurrentDirectory() + "\\" + fileName)){

			load_file(Directory.GetCurrentDirectory() + "\\" + fileName);
			WriteTo();
		}
		else{

			Console.WriteLine("file does not exist: {0}\\{1}",Directory.GetCurrentDirectory() ,fileName);
			Console.Read();
		}
	}

	static void writeToConsole(){

		string [][] sentents = new string[textArray.Count][];
		int index = 0;
		foreach(string line in textArray){

			sentents[index] = line.Split(null);
			Console.WriteLine("{0}-{1}", sentents[index].Length,string.Join("******",sentents[index]));
			index ++;
		}
	}

	static void writeToFile(){

		StreamWriter fwriter = File.CreateText("write_file.txt");
		string [][] sentents = new string[textArray.Count][];
		int index = 0;
		foreach(string line in textArray){

			sentents[index] = line.Split(null);
			fwriter.WriteLine("{0}-{1}", sentents[index].Length,string.Join("******",sentents[index]));
			index ++;
		}
		fwriter.Close();
	}

	static void display_usage(){

		string usage = @"usage: WordCount [-c] [-f] [-h] textfile.txt
    	where [] indicates an optonal argument
		-c print to console
		-f write to a file
		-h prints this message";
		Console.WriteLine(usage);
	}

	static void load_file(string file){

		StreamReader freader = File.OpenText(file);
		string text_line;

		while( (text_line= freader.ReadLine()) != null){

			if(text_line.Length > 0){

				textArray.Add(text_line);
				//Console.WriteLine("{0}({2}): {1}", textArray.Count, text_line, text_line.Length);
				continue;
			}
		}
		freader.Close();
	}

}

}