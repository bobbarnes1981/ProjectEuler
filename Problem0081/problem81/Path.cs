using System.Collections.Generic;
using System.Linq;

namespace Problem81
{
    class Path
    {
        private List<Cell> m_cells;

        public Path()
            : this(new List<Cell>())
        {
        }

        public Path(Cell cell)
            : this(new List<Cell> { cell })
        {
        }

        public Path(List<Cell> cells)
        {
            m_cells = cells;
        }

        public int Sum
        {
            get
            {
                return m_cells.Sum(x => x.Value);
            }
        }

        public string Direction { get; set; }

        public void Prepend(Cell cell)
        {
            m_cells.Insert(0, cell);
        }

        public void Append(Cell cell)
        {
            m_cells.Add(cell);
        }

        public Path Clone()
        {
            List<Cell> cells = new List<Cell>();

            foreach (Cell cell in m_cells)
            {
                cells.Add(cell);
            }

            return new Path(cells);
        }

        public void Highlight(bool highlight)
        {
            foreach (Cell cell in m_cells)
            {
                cell.Highlight = highlight;
            }
        }
    }
}
