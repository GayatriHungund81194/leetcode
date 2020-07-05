public static int minimumDistance(int numRows, int numColumns, char[,] area)
    {
        int noofpass = 0;

        for (int i = 0; i < numRows; i++)
        {
            for (int j = 0; j < numColumns; j++)
            {
                noofpass = noofpass + 1;
                if (area[i, j] == 'O' || area[i, j] == 'D')
                {
                    break;
                }
            }
        }
        return noofpass;
    }