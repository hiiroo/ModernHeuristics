"""
MIT License

Copyright (c) 2019 Ali Mert Ceylan, Adopted from original resources provided
by Korhan Karabulut for COMP 5658 Modern Heuristics Course

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from math import sqrt

class TSPInstance:

    """
    private int n;
    private int[][] distance;
    private String problemName;

    public TSPInstance( String problemName ) {
        this.problemName = problemName;
        readData();
    }
    """
    def __init__(self, problem_name):
        self.problem_name = problem_name
        self.distance = self.read_data();


    """
    public void readData() {
        try ( Scanner input = new Scanner( new File( problemName ) ) ) {
            //skip first 3 lines
            for ( int i = 0; i < 3; i++ ) {
                input.nextLine();
            }
            //skip one word
            input.next();
            //read dimension
            n = input.nextInt();
            //skip first 2 lines
            for ( int i = 0; i < 3; i++ ) {
                input.nextLine();
            }

            double xcoords[] = new double[n];
            double ycoords[] = new double[n];
            //read coordinates
            for ( int i = 0; i < n; i++ ) {
                //skip #node
                input.next();
                xcoords[ i ] = Double.parseDouble( input.next());
                ycoords[ i ] =  Double.parseDouble( input.next());
            }
            input.close();
            distance = new int[n][n];
            //calculate Euclidean distance
            for ( int i = 0; i < n; i++ ) {
                for ( int j = 0; j < n; j++ ) {
                    if ( i == j ) continue;
                    
                    distance[i][j]=(int) ( Math.sqrt( Math.pow ( xcoords[i]-xcoords[j],2) 
                    + Math.pow ( ycoords[i]-ycoords[j],2)) + 0.5);
                }
            }
            
        } catch ( FileNotFoundException ex ) {
            System.out.println( "File cannot be openned." );
        }
    }
    """
    def read_data(self):
        with open(self.problem_name, "r") as data_file:
            data_file_lines = data_file.readlines()
            
            cleaner = lambda x:x.split(" ")[-1]
            data_cleaner = lambda x:[float(co_ax) for co_ax in x.rstrip("\n").split()]

            name, type, desc, dims, ewtp = map(cleaner, data_file_lines[0:5])
            coords = [data_cleaner(data_line) for data_line in data_file_lines[6:-1]]

        grid = [[sqrt(pow(coords[i][0] - coords[j][0], 2) + pow(coords[i][1] - coords[j][1], 2)) for j in range(len(coords))] for i in range(len(coords))]
        return grid


    # """
    # public int getDistance( int city1, int city2 ) {
    #     return distance[ city1 ][ city2 ];
    # }
    # """
    # def distance(self, city1:int, city2:int):
    #     return self.distance[city1][city2]

"""
public class TSPInstance {

    private void calculateGEODistance(double[] xcoords, double[] ycoords) {
        double latitude[] = new double[n];
        double longitude[] = new double[n];
        //calculate distance matrix
        for ( int i = 0; i < n; i++ ) {
            int deg = ( int ) (xcoords[ i ] + 0.5);
            double min = xcoords[ i ] - deg;
            latitude[ i ] = Math.PI * (deg + 5.0 * min / 3.0) / 180.0;
            deg = ( int ) (ycoords[ i ] + 0.5);
            min = ycoords[ i ] - deg;
            longitude[ i ] = Math.PI * (deg + 5.0 * min / 3.0) / 180.0;

        }

        for ( int i = 0; i < n; i++ ) {
            for ( int j = 0; j < n; j++ ) {
                if ( i == j ) {
                    continue;
                }
                double RRR = 6378.388;
                double q1 = Math.cos( longitude[ i ] - longitude[ i ] );
                double q2 = Math.cos( latitude[ i ] - latitude[ j ] );
                double q3 = Math.cos( latitude[ i ] + latitude[ j ] );
                distance[ i ][ j ] = ( int ) (RRR * Math.acos( 0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3) ) + 1.0);
            }
        }
    }
}
"""
