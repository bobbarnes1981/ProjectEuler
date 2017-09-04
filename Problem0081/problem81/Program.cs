namespace Problem81
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //p081_matrix.txt
            //p081_example.txt
            string filename = "p081_matrix.txt";

            new Visualizer(new Matrix(filename)).Solve();
        }
    }
}
