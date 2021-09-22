package capitulo5EstruturaRepeticao;

import javax.swing.JOptionPane;

public class Exemplo5_3For {
    public static void main(String[] args) {
        float num, media, soma;
        int cont;
        cont = 0;
        soma = 0f;
        for (cont = 0; cont < 3; cont++) {
            num = Float.parseFloat(JOptionPane.showInputDialog("Digite um numero"));
            soma += num;
        }
        media = soma / cont;
        JOptionPane.showMessageDialog(null, "A média é: " + media);
    }
}