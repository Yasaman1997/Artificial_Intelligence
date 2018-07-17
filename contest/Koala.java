package players;

import game.AbstractPlayer;
import game.BoardSquare;
import game.OthelloGame;
import game.OthelloPlayer;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

public class Koala extends AbstractPlayer {
    private static final OthelloGame GAME = new OthelloGame();
    private static final DefaultHeuristic HEURISTIC = new DefaultHeuristic();
    private int[][][] tmpBoards;

    public Koala() {
        this(7);
    }

    public Koala(int depth) {
        super(depth);
        this.tmpBoards = new int[getDepth() + 1][8][8];
    }

    @Override
    public BoardSquare play(int[][] board) {
        BoardSquare bestMove = new BoardSquare(-1, -1); // No Move
        double bestMoveScore = Double.NEGATIVE_INFINITY;

        int ply = getDepth();
        final double lower = Double.POSITIVE_INFINITY;
        double upper = Double.NEGATIVE_INFINITY;

        for (BoardSquare move : Utils.getPossibleMoves(board, getMyBoardMark(), GAME)) {
            Utils.copy_(tmpBoards[ply], board);
            GAME.do_move(tmpBoards[ply], move, this);
            double moveScore = minSearch(tmpBoards[ply], lower, upper, ply - 1);
            upper = Math.max(moveScore, upper);
            if (moveScore > bestMoveScore) {
                bestMove = move;
                bestMoveScore = moveScore;
            }
        }

        return bestMove;
    }

    private double maxSearch(int[][] board, final double lower, double upper, int ply) {
        if (ply < 0) {
            return HEURISTIC.evaluate(board, getMyBoardMark());
        }

        List<BoardSquare> moves = Utils.getPossibleMoves(board, getMyBoardMark(), GAME);
        if (moves.isEmpty()) return minSearch(board, lower, upper, ply - 1);

        double score = Double.NEGATIVE_INFINITY;
        for (BoardSquare move : moves) {
            Utils.copy_(tmpBoards[ply], board);
            GAME.do_move(tmpBoards[ply], move, this);
            double moveScore = minSearch(tmpBoards[ply], lower, upper, ply - 1);

            score = Math.max(moveScore, score);
            upper = Math.max(moveScore, upper);

            if (moveScore > lower) break;
        }

        return score;
    }

    private double minSearch(int[][] board, double lower, final double upper, int ply) {
        if (ply < 0) {
            return HEURISTIC.evaluate(board, getMyBoardMark());
        }
        int mark = this.getBoardMark();

        List<BoardSquare> moves = Utils.getPossibleMoves(board, getOpponentBoardMark(), GAME);

        if (moves.isEmpty()) return maxSearch(board, lower, upper, ply - 1);

        double score = Double.POSITIVE_INFINITY;
        for (BoardSquare move : moves) {
            Utils.copy_(tmpBoards[ply], board);


            this.setBoardMark(-mark);
            this.setOpponentBoardMark(mark);
            GAME.do_move(tmpBoards[ply], move, this);
            this.setBoardMark(mark);
            this.setOpponentBoardMark(-mark);


            double moveScore = maxSearch(tmpBoards[ply], lower, upper, ply - 1);

            score = Math.min(moveScore, score);
            lower = Math.min(moveScore, lower);

            if (moveScore < upper) break;
        }

        return score;
    }

    public static class DefaultHeuristic {
        private static final long serialVersionUID = 1283719271L;

        private double[][] valueMatrix = new double[][]{
                new double[]{4.229822185968378, 0.7364823093608387, -0.43659510264698387, 1.2899013024419785, 1.2899013024419785, -0.43659510264698387, 0.7364823093608387, 4.229822185968378},
                new double[]{0.7364823093608387, -1.6557990153138487, -0.7529151358857147, 0.09912135791174807, 0.09912135791174807, -0.7529151358857147, -1.6557990153138487, 0.7364823093608387},
                new double[]{-0.43659510264698387, -0.7529151358857147, 0.8686418951701064, 0.006024118380231561, 0.006024118380231561, 0.8686418951701064, -0.7529151358857147, -0.43659510264698387},
                new double[]{1.2899013024419785, 0.09912135791174807, 0.006024118380231561, 0.5141534259263218, 0.5141534259263218, 0.006024118380231561, 0.09912135791174807, 1.2899013024419785},
                new double[]{1.2899013024419785, 0.09912135791174807, 0.006024118380231561, 0.5141534259263218, 0.5141534259263218, 0.006024118380231561, 0.09912135791174807, 1.2899013024419785},
                new double[]{-0.43659510264698387, -0.7529151358857147, 0.8686418951701064, 0.006024118380231561, 0.006024118380231561, 0.8686418951701064, -0.7529151358857147, -0.43659510264698387},
                new double[]{0.7364823093608387, -1.6557990153138487, -0.7529151358857147, 0.09912135791174807, 0.09912135791174807, -0.7529151358857147, -1.6557990153138487, 0.7364823093608387},
                new double[]{4.229822185968378, 0.7364823093608387, -0.43659510264698387, 1.2899013024419785, 1.2899013024419785, -0.43659510264698387, 0.7364823093608387, 4.229822185968378}};
        private double mobilityW = 1.3832779555883032;
        private double differenceW = -1.3245453490596095;
        private double frontierW = -2.512709251582406;

        public double evaluate(int[][] board, int mark) {
            double score = 0;
            score += HeuristicUtils.boardScore(board, mark, valueMatrix);
            score += mobilityW * HeuristicUtils.mobility(board, mark);
            score += differenceW * HeuristicUtils.difference(board, mark);
            score += frontierW * HeuristicUtils.frontier(board, mark);
            return score;
        }
    }

    public static class Utils {
        public static int[][] copy(int[][] board) {
            int[][] newBoard = new int[board.length][];
            for (int i = 0; i < board.length; i++) {
                newBoard[i] = new int[board[i].length];
                for (int j = 0; j < board[i].length; j++)
                    newBoard[i][j] = board[i][j];
            }
            return newBoard;
        }

        public static double[][] copy(double[][] w) {
            double[][] nw = new double[w.length][];
            for (int i = 0; i < w.length; i++) {
                nw[i] = new double[w[i].length];
                System.arraycopy(w[i], 0, nw[i], 0, w[i].length);
            }
            return nw;
        }

        public static void copy_(int[][] dest, int[][] source) {
            for (int i = 0; i < source.length; i++) {
                int[] destRow = dest[i];
                int[] sourceRow = source[i];
                System.arraycopy(sourceRow, 0, destRow, 0, source[i].length);
            }
        }

        public static void copy_(double[][] dest, double[][] source) {
            for (int i = 0; i < source.length; i++) {
                double[] destRow = dest[i];
                double[] sourceRow = source[i];
                System.arraycopy(sourceRow, 0, destRow, 0, source[i].length);
            }
        }

        public static double norm(double[][] w) {
            int n = 0;
            for (int i = 0, wLength = w.length; i < wLength; i++) n += w[i].length;

            double r = 0;
            for (int i = 0; i < w.length; i++) {
                for (int j = 0; j < w[i].length; j++) {
                    double v = w[i][j];
                    r += v * v / n;
                }
            }

            return r;
        }

        public static double[][] add_(double[][] a, double[][] b) {
            for (int i = 0; i < a.length; i++) {
                double[] ai = a[i];
                double[] bi = b[i];
                for (int j = 0; j < a[i].length; j++) {
                    ai[j] += bi[j];
                }
            }
            return a;
        }

        public static double[][] add_(double[][] a, double b) {
            for (int i = 0; i < a.length; i++) {
                double[] ai = a[i];
                for (int j = 0; j < a[i].length; j++) {
                    ai[j] += b;
                }
            }
            return a;
        }

        public static double[][] mult_(double[][] m, double a) {
            for (int i = 0; i < m.length; i++) {
                double[] mi = m[i];
                for (int j = 0; j < m[i].length; j++) {
                    mi[j] *= a;
                }
            }
            return m;
        }

        public static double[][] randn_(double[][] m, int mean, int std) {
            ThreadLocalRandom random = ThreadLocalRandom.current();
            for (int r = 0; r < m.length; r++) {
                double[] row = m[r];
                for (int c = 0; c < row.length; c++) {
                    row[c] = random.nextGaussian() * std + mean;
                }
            }
            return m;
        }

        public static double[][] rand01_(double[][] m) {
            ThreadLocalRandom random = ThreadLocalRandom.current();
            for (int r = 0; r < m.length; r++) {
                double[] row = m[r];
                for (int c = 0; c < row.length; c++) {
                    row[c] = random.nextBoolean() ? 1 : 0;
                }
            }
            return m;
        }

        public static double[][] addRandn_(double[][] m, int mean, int std) {
            ThreadLocalRandom random = ThreadLocalRandom.current();
            for (int r = 0; r < m.length; r++) {
                double[] row = m[r];
                for (int c = 0; c < row.length; c++) {
                    row[c] += random.nextGaussian() * std + mean;
                }
            }
            return m;
        }

        public static double[][] fill_(double[][] m, double value) {
            for (int r = 0; r < m.length; r++) {
                double[] row = m[r];
                for (int c = 0; c < row.length; c++) {
                    row[c] = value;
                }
            }
            return m;
        }

        public static double[][] matrix(int height, int width) {
            return new double[height][width];
        }

        public static double[][] tileBoardQ1_(double[][] board) {
            for (int r = 0; r < 4; r++) {
                for (int c = 0; c < 4; c++) {
                    board[7 - r][7 - c] = board[r][c];
                    board[7 - r][c] = board[r][c];
                    board[r][7 - c] = board[r][c];
                }
            }
            return board;
        }

        public static double[][] tileDiagonally_(double[][] board) {
            for (int r = 0; r < 8; r++) {
                for (int c = r + 1; c < 8; c++) {
                    board[r][c] = board[c][r];
                }
            }
            return board;
        }

        public static void printBoardWeights(double[][] board) {
            String divider = new String("\r\n");
            int width = 6;
            String d = "--";
            for (int i = 0; i < width; i++) d += "-";
            for (int i = 0; i < (8 - 1); i++) divider += d + "+";
            divider += d;

            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8; j++) {
                    System.out.printf(" %+6.2f %c", board[i][j], (j == (8 - 1)) ? ' ' : '|');
                }
                if (i != 8 - 1) {
                    System.out.println(divider);
                }
            }
            System.out.println("\r\n");
        }

        public static int hash(double[][] m) {
            StringBuilder b = new StringBuilder();
            for (double[] d : m) {
                for (double e : d) {
                    b.append(e).append(" ");
                }
            }
            return b.toString().hashCode();
        }

        public static void printBoard(int[][] board) {
            char[] conversion = {'o', ' ', 'x'};

            String d = "\r\n";
            for (int i = 0; i < 7; i++) {
                d += "---+";
            }
            d += "---";

            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8; j++) {
                    System.out.printf(" %c %c", conversion[board[i][j] + 1], (j == 7) ? ' ' : '|');
                }
                if (i != 8 - 1) {
                    System.out.println(d);
                }
            }
            System.out.println("\r\n");
        }

        public static List<BoardSquare> getPossibleMoves(int[][] board, int mark, OthelloGame game) {
            List<BoardSquare> moves = new ArrayList<>();
            OthelloPlayer othelloPlayer = new OthelloPlayer(-1);
            othelloPlayer.setBoardMark(mark);
            int sizeI = board.length;
            for (int i = 0; i < sizeI; i++) {
                for (int j = 0; j < sizeI; j++) {
                    BoardSquare moviment = new BoardSquare(i, j);
                    if (game.validate_moviment(board, moviment, othelloPlayer) == 0) {
                        moves.add(moviment);
                    }
                }
            }
            return moves;
        }

        public static boolean hasPossibleMoves(int[][] board, int mark, OthelloGame game) {
            OthelloPlayer othelloPlayer = new OthelloPlayer(-1);
            othelloPlayer.setBoardMark(mark);
            int sizeI = board.length;
            for (int i = 0; i < sizeI; i++) {
                for (int j = 0; j < sizeI; j++) {
                    BoardSquare moviment = new BoardSquare(i, j);
                    if (game.validate_moviment(board, moviment, othelloPlayer) == 0) {
                        return true;
                    }
                }
            }
            return false;
        }

        public static int countPossibleMoves(int[][] board, int mark, OthelloGame game) {
            int nMoves = 0;
            OthelloPlayer othelloPlayer = new OthelloPlayer(-1);
            othelloPlayer.setBoardMark(mark);
            int sizeI = board.length;
            for (int i = 0; i < sizeI; i++) {
                for (int j = 0; j < sizeI; j++) {
                    BoardSquare moviment = new BoardSquare(i, j);
                    if (game.validate_moviment(board, moviment, othelloPlayer) == 0) {
                        nMoves++;
                    }
                }
            }
            return nMoves;
        }
    }

    public static class HeuristicUtils {
        public static final OthelloGame GAME = new OthelloGame();

        private static double normalizeMetric(int mine, int opponent) {
            if (mine + opponent == 0) return 0;
            return mine > opponent ?
                    mine / (double) (mine + opponent) :
                    -opponent / (double) (mine + opponent);
        }

        public static double mobility(int[][] board, int mark) {
            int myMoves = Utils.countPossibleMoves(board, mark, GAME);
            int oppoentMoves = Utils.countPossibleMoves(board, -mark, GAME);
            return normalizeMetric(myMoves, oppoentMoves);
        }

        public static double difference(int[][] board, int mark) {
            int myMarks = countMarks(board, mark);
            int opponentMarks = countMarks(board, -mark);
            return normalizeMetric(myMarks, opponentMarks);
        }

        public static double frontier(int[][] board, int mark) {
            int myMarks = countSurfaceMarks(board, mark);
            int opponentMarks = countSurfaceMarks(board, -mark);
            return normalizeMetric(myMarks, opponentMarks);
        }

        public static int countMarks(int[][] board, int mark) {
            int nMarks = 0;
            for (int r = 0; r < board.length; r++) {
                for (int c = 0; c < board[0].length; c++) {
                    if (board[r][c] == mark)
                        nMarks++;
                }
            }
            return nMarks;
        }

        public static int countSurfaceMarks(int[][] board, int mark) {
            int dr[] = {0, 1, 1, 0, -1, -1, 1, -1};
            int dc[] = {1, 0, 1, -1, 0, -1, -1, 1};

            int nSurface = 0;
            for (int r = 0; r < 8; r++) {
                for (int c = 0; c < 8; c++) {
                    if (board[r][c] != mark) continue;
                    for (int i = 0; i < 8; i++) {
                        int nr = r + dr[i];
                        int nc = c + dc[i];
                        if (nr > 7 || nr < 0) continue;
                        if (nc > 7 || nc < 0) continue;

                        if (board[nr][nc] == 0) nSurface++;
                        break;
                    }
                }
            }

            return nSurface;
        }

        public static double[][] createValueMatrix() {
            double[][] mat = Utils.matrix(8, 8);
            Utils.randn_(mat, 0, 1);
            Utils.tileDiagonally_(mat);
            Utils.tileBoardQ1_(mat);
            return mat;
        }

        public static double[][] mutateValueMatrix(double[][] mat, double p) {
            ThreadLocalRandom random = ThreadLocalRandom.current();
            for (int r = 0; r < 4; r++) {
                for (int c = r; c < 4; c++) {
                    if (random.nextDouble() < p) {
                        mat[r][c] += random.nextGaussian();
                    }
                }
            }
            Utils.tileDiagonally_(mat);
            Utils.tileBoardQ1_(mat);
            return mat;
        }

        public static double boardScore(int[][] board, int mark, double[][] valueMatrix) {
            double score = 0;
            for (int r = 0; r < 8; r++) {
                for (int c = 0; c < 8; c++) {
                    if (board[r][c] == mark) {
                        score += valueMatrix[r][c];
                    }
                    if (board[r][c] == -mark) {
                        score -= valueMatrix[r][c];
                    }
                }
            }
            return score;
        }
    }
}
