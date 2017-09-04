using SdlDotNet.Core;
using SdlDotNet.Graphics;
using SdlDotNet.Graphics.Primitives;
using System;
using System.Drawing;
using System.Threading;

namespace Problem81
{
    class Visualizer
    {
        private Matrix m_matrix;

        private Surface m_video;

        private Thread m_worker;

        public Visualizer(Matrix matrix)
        {
            m_matrix = matrix;
        }

        public void Solve()
        {

            m_video = Video.SetVideoMode(400, 400);

            m_worker = new Thread(worker);

            Events.Quit += Events_Quit;
            Events.Tick += Events_Tick;

            m_worker.Start();

            Events.Run();
        }

        private void worker()
        {
            ISolver solver;

            solver = new NearestNeighbour(m_matrix);
            int n = solver.Solve();
            Console.WriteLine("Nearest neighbour route: {0}", n);

            solver = new DepthFirst(m_matrix);
            int m = solver.Solve();
            Console.WriteLine("Depth first route: {0}", m);
        }

        private void Events_Tick(object sender, TickEventArgs e)
        {
            SdlDotNet.Graphics.Font f = new SdlDotNet.Graphics.Font("c:\\windows\\fonts\\cour.ttf", 16);

            int width = m_video.Width / m_matrix.Width;
            int height = m_video.Height / m_matrix.Height;

            for (int y = 0; y < m_matrix.Height; y++)
            {
                for (int x = 0; x < m_matrix.Width; x++)
                {
                    Cell cell = m_matrix[x, y];
                    Color colour;
                    if (cell.Highlight)
                    {
                        colour = Color.FromArgb(cell.ColourValue, 0, cell.ColourValue);
                    }
                    else if (cell.Visited)
                    {
                        colour = Color.FromArgb(0, 0, cell.ColourValue);
                    }
                    else if (cell.Active)
                    {
                        colour = Color.FromArgb(0, cell.ColourValue, 0);
                    }
                    else
                    {
                        colour = Color.FromArgb(cell.ColourValue, 0, 0);
                    }
                    m_video.Draw(new Box(new Point(x * width, y * height), new Size(width - 1, height - 1)), colour, false, true);

                    if (cell.Active)
                    {
                        //m_video.Draw(new Box(new Point(x * width, y * height), new Size(width-1, height-1)), Color.White, false, false);
                    }

                    if (width >= 10 && height >= 10)
                    {
                        m_video.Blit(f.Render(string.Format("{0}", cell.Value), Color.White), new Point(x * width, (y * height) + (height / 2) - 10));
                        m_video.Blit(f.Render(string.Format("{0} {1}", cell.Shortest == null ? "" : cell.Shortest.Sum.ToString(), cell.Shortest == null ? "" : cell.Shortest.Direction), Color.White), new Point(x * width, (y * height) + (height / 2)));
                    }
                }
            }

            m_video.Update();
        }

        private void Events_Quit(object sender, QuitEventArgs e)
        {
            Events.QuitApplication();
        }
    }
}
