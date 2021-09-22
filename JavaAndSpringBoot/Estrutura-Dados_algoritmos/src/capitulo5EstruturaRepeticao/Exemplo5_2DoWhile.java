package capitulo5EstruturaRepeticao;

import javax.swing.JOptionPane;

public class Exemplo5_2DoWhile {
    public static void main(String[] args) {
        float num, soma = 0f;
        do {
            num = Float.parseFloat(JOptionPane.showInputDialog("Digite um numero ou zero para sair"));
            soma += num;
            JOptionPane.showMessageDialog(null, "A soma é: " + soma);
        } while (num != 0);
    }
}