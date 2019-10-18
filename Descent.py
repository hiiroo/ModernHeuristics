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
from tqdm import tqdm
from BooleanGenome import BooleanGenome, BooleanFunction

"""
public class Descent {
    public void run(int tMax) {

        BooleanGenome best = null;
        BooleanFunction function = new BooleanFunction();
        for ( int t = 0; t < tMax; t++ ) {
            boolean local = false;
            while (!local) {
                BooleanGenome vc = new BooleanGenome(4, function );
                if ( vc.getValue() ) break;
                BooleanGenome vn = vc.getBestNeighbor();
                if ( vn!=null ) {
                    best= vn;
                    break;
                }
                local = true;
            }
            if ( !local ) {
                System.out.println( best );
                return;
            }
        }
    }
}

"""
class Descent:
    @staticmethod
    def optimize(tMax:int):
        bbest = None
        bfunction = BooleanFunction();

        for i in tqdm(range(tMax)):
            blocal = False
            while(not blocal):
                vc = BooleanGenome(4, bfunction)
                if(vc.value):
                    break
                vn = vc.best_neighbor()

                if(vn is not None):
                    bbest = vn
                    break
                blocal = True
            if(not blocal):
                if (bbest is not None):
                    print(bbest)

                return
