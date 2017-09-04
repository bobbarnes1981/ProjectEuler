using System.IO;

namespace Problem81
{
    class Matrix
    {
        private int m_minimumValue;
        private int m_maximumValue;
        private int m_range;
        private int m_multiplier;

        private Cell[][] m_cells;

        public Matrix(string path)
        {
            m_minimumValue = int.MaxValue;
            m_maximumValue = int.MinValue;

            string[] rows = File.ReadAllLines(path);

            m_cells = new Cell[rows.Length][];
            for (int r = 0; r < rows.Length; r++)
            {
                string[] cols = rows[r].Split(',');
                m_cells[r] = new Cell[cols.Length];
                for (int c = 0; c < cols.Length; c++)
                {
                    int val = int.Parse(cols[c]);
                    m_cells[r][c] = new Cell(c, r, val);
                    if (val < m_minimumValue)
                    {
                        m_minimumValue = val;
                    }
                    if (val > m_maximumValue)
                    {
                        m_maximumValue = val;
                    }
                }
            }

            m_range = m_maximumValue - m_minimumValue;

            m_multiplier = (m_range / 256) + 1;

            for (int y = 0; y < Height; y++)
            {
                for (int x = 0; x < Width; x++)
                {
                    this[x, y].ColourValue = (this[x, y].Value - m_minimumValue) / m_multiplier;
                }
            }
        }

        public Cell this[int x, int y]
        {
            get
            {
                return m_cells[y][x];
            }
        }

        public int Width
        {
            get
            {
                return m_cells[0].Length;
            }
        }

        public int Height
        {
            get
            {
                return m_cells.Length;
            }
        }
    }
}
