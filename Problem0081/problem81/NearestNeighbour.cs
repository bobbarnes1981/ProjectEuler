using System.Threading;

namespace Problem81
{
    class NearestNeighbour : ISolver
    {
        private int m_delay = 20;

        private Matrix m_matrix;

        public NearestNeighbour(Matrix matrix)
        {
            m_matrix = matrix;
        }

        public int Solve()
        {
            return solve(0, 0, 0);
        }

        private int solve(int x, int y, int total)
        {
            m_matrix[x, y].Active = true;
            Thread.Sleep(m_delay);

            total += m_matrix[x, y].Value;
            Cell c = null;
            if (y + 1 < m_matrix.Height)
            {
                c = m_matrix[x, y + 1];
            }
            if (x + 1 < m_matrix.Width)
            {
                Cell other = m_matrix[x + 1, y];
                if (c == null || other.Value < c.Value)
                {
                    c = other;
                }
            }
            if (c != null)
            {
                total = solve(c.X, c.Y, total);
            }

            Thread.Sleep(m_delay);
            m_matrix[x, y].Active = false;

            return total;
        }
    }
}
