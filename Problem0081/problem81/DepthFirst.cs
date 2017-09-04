using System;
using System.Threading;

namespace Problem81
{
    class DepthFirst : ISolver
    {
        private int m_delay = 20;

        private int m_flash = 250;

        private int m_shortest= int.MaxValue;

        private Matrix m_matrix;

        public DepthFirst(Matrix matrix)
        {
            m_matrix = matrix;
        }

        public int Solve()
        {
            return solve(0, 0, 0, new Path());
        }

        private int solve(int x, int y, int total, Path path)
        {
            // set current cell active
            m_matrix[x, y].Active = true;
            Thread.Sleep(m_delay);

            if (m_matrix[x, y].Shortest != null)
            {
                // we already have a calculated shortest route from here to destination

                total += m_matrix[x, y].Shortest.Sum;

                // have we found a new shortest route
                checkShortest(total);

                // display full route
                displayPath(path, m_matrix[x, y].Shortest);
            }
            else
            {
                // we do not have a shortest route calculated, let's calculate one

                total += m_matrix[x, y].Value;

                if (y + 1 == m_matrix.Height && x + 1 == m_matrix.Width)
                {
                    // we are at the destination

                    m_matrix[x, y].Shortest = new Path(m_matrix[x, y]);
                    m_matrix[x, y].Visited = true;

                    // have we found a new shortest route
                    checkShortest(total);

                    // display full route
                    displayPath(path, m_matrix[x, y].Shortest);
                }
                else
                {
                    int downMinValue = int.MaxValue;
                    Path downMinPath = null;

                    int rightMinValue = int.MaxValue;
                    Path rightMinPath = null;

                    // check 'all' neighbours (right/down)

                    if (y + 1 < m_matrix.Height)
                    {
                        Path p = path.Clone();
                        p.Append(m_matrix[x, y]);
                        downMinValue = solve(x, y + 1, total, p);
                        downMinPath = m_matrix[x, y + 1].Shortest;
                    }
                    if (x + 1 < m_matrix.Width)
                    {
                        Path p = path.Clone();
                        p.Append(m_matrix[x, y]);
                        rightMinValue = solve(x + 1, y, total, p);
                        rightMinPath = m_matrix[x + 1, y].Shortest;
                    }

                    if (downMinValue < rightMinValue)
                    {
                        // down is shortest route

                        m_matrix[x, y].Shortest = downMinPath.Clone();
                        m_matrix[x, y].Shortest.Prepend(m_matrix[x, y]);
                        m_matrix[x, y].Shortest.Direction = "V";
                        m_matrix[x, y].Visited = true;

                        total = downMinValue;
                    }
                    else
                    {
                        // right is shortest route

                        m_matrix[x, y].Shortest = rightMinPath.Clone();
                        m_matrix[x, y].Shortest.Prepend(m_matrix[x, y]);
                        m_matrix[x, y].Shortest.Direction = ">";
                        m_matrix[x, y].Visited = true;

                        total = rightMinValue;
                    }
                }
            }

            // set current cell inactive
            Thread.Sleep(m_delay);
            m_matrix[x, y].Active = false;

            // return total distance
            return total;
        }

        private void checkShortest(int value)
        {
            Console.WriteLine("Check shortest: {0}", value);
            if (value < m_shortest)
            {
                m_shortest = value;
                Console.WriteLine("Current minimum: {0}", m_shortest);
            }
        }

        private void displayPath(Path to, Path from)
        {
            to.Highlight(true);
            from.Highlight(true);
            Thread.Sleep(m_flash);
            to.Highlight(false);
            from.Highlight(false);
        }
    }
}
