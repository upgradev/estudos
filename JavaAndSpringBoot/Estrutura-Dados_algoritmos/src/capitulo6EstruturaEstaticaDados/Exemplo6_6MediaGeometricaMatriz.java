package capitulo6EstruturaEstaticaDados;

import javax.swing.JOptionPane;

public class Exemplo6_6MediaGeometricaMatriz {
    public static void main(String[] args) {
        int G[][] = new int[6][2];
        double prod;
        String num;
        try {
            // store in matrix
            for (int i = 0; i < 6; i++) {
                for (int j = 0; j < 2; j++) {
                    num = JOptionPane.showInputDialog("Informar o valor de G" + i + ", " + j + ":");
                    G[i][j] = Integer.parseInt(num);
                }
            }

            // calculate prod
            for (int i = 0; i < 6; i++) {
                prod = 1;
                for (int j = 0; j < 2; j++) {
                    prod *= G[i][j];
                }
                JOptionPane.showMessageDialog(null, "Linha " + i + ": " + Math.sqrt(prod));
            }
        } catch (Exception e) {
            // TODO: handle exception
            JOptionPane.showMessageDialog(null, "Erro:  " + e);
        }
    }
}