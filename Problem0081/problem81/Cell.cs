namespace Problem81
{
    class Cell
    {
        public int Value { get; private set; }

        public int ColourValue { get; set; }

        public bool Active { get; set; }

        public bool Visited { get; set; }

        public bool Highlight { get; set; }

        public int X { get; set; }

        public int Y { get; set; }

        public Path Shortest { get; set; }

        public Cell(int x, int y, int value)
        {
            X = x;
            Y = y;
            Value = value;
            Active = false;
            Visited = false;
            Highlight = false;
            Shortest = null;
        }
    }
}
