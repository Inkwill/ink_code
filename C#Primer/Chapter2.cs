namespace CSharpPrimer{

using System;
using System.IO;
using System.Collections;

class Chapter2{

	public static void Main(string[] args){

		//public string query_key;
		string query_key;
		Console.Write("Please enter a query or 'q' to Quit: ");
		query_key = Console.ReadLine();
		Query q = new Query(query_key);
		q.eval();
		q.print_solution();
		Console.Read();
	}
}

class Query{

	public string key; 
	public Query(string query_key){

		key = query_key;
	}
	virtual public void eval(){

		Console.WriteLine("Your input query: {0}",key);
	}

	virtual public void print_solution(){
		Console.WriteLine(true.GetType());
	}
}

/*class NameQuery : Query{}
class NotQuery : Query{}
class OrQuery : Query{}
class AndQuery : Query{}*/


}
