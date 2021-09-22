package capitulo6EstruturaEstaticaDados;

import javax.swing.JOptionPane;

public class Exemplo6_7MediaNotaAlunosMatriz {
    public static void main(String[] args) {
        final int nProvas = 3;
        final int nAlunos = 5;
        float[][] notaProva = new float[nAlunos][nProvas];

        float[] MedAlunos = new float[nAlunos];
        float[] MedProvas = new float[nProvas];

        float Soma;
        String num;

        try {

            for (int i = 0; i < nAlunos; i++) {
                Soma = 0;
                for (int j = 0; j < nProvas; j++) {
                    num = JOptionPane.showInputDialog("Entre nota aluno-" + i + "Prova " + j);
                    notaProva[i][j] = Float.parseFloat(num);
                    Soma = Soma + notaProva[i][j];
                }
                MedAlunos[i] = Soma / nProvas;
            }
            for (int j = 0; j < nProvas; j++) {
                Soma = 0;
                for (int i = 0; i < nAlunos; i++) {
                    Soma = Soma + notaProva[i][j];
                }
                MedProvas[j] = Soma / nAlunos;
            }
            for (int i = 0; i < nAlunos; i++) {
                JOptionPane.showMessageDialog(null, "Media do aluno " + i + ": " + MedAlunos[i]);
            }

            for (int i = 0; i < nProvas; i++) {
                JOptionPane.showMessageDialog(null, "Media do Provas " + i + ": " + MedProvas[i]);
            }

        } catch (Exception e) {
        }

    }
}