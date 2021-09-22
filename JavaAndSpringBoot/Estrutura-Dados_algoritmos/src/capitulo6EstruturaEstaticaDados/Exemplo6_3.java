package capitulo6EstruturaEstaticaDados;

import javax.swing.JOptionPane;

public class Exemplo6_3 {
    public static void main(String[] args) {

        int[] vetorA = new int[5];
        int soma = 0;
        String num;
        try {
            for (int i = 0; i < vetorA.length; i++) {
                num = JOptionPane.showInputDialog("Digite o numero " + i + ": ");
                int numero = Integer.parseInt(num);
                vetorA[i] = numero;
            }
            for (int i = 0; i < vetorA.length; i++) {
                if (vetorA[i] % 2 != 0) {
                    soma += vetorA[i];
                }

            }
            JOptionPane.showMessageDialog(null, "Soma dos ímpares: " + soma);

        } catch (Exception e) {
            // TODO: handle exception
        }

    }
}