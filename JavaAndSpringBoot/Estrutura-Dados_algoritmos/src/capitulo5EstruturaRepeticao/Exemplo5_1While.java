package capitulo5EstruturaRepeticao;

import javax.swing.JOptionPane;

public class Exemplo5_1While {

    public static void main(String[] args) {

        float num, media, soma;
        int cont;
        cont = 0;
        soma = 0f;

        while (cont < 20) {
            num = Float.parseFloat(JOptionPane.showInputDialog("Digite um numero"));
            soma = soma + num;
            cont = cont + 1;
        }

        media = soma / cont;
        JOptionPane.showMessageDialog(null, "A média é: " + media);

    }
}