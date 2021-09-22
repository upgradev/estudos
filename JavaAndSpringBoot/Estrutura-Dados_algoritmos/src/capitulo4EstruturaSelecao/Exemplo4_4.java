package capitulo4EstruturaSelecao;

import javax.swing.JOptionPane;

public class Exemplo4_4 {

    public static void main(String[] args) {
        int valor1, valor2, soma;

        valor1 = Integer.parseInt(JOptionPane.showInputDialog("Qual o primeiro valor: "));
        valor2 = Integer.parseInt(JOptionPane.showInputDialog("Qual o segundo valor: "));
        soma = valor1 + valor2;

        JOptionPane.showMessageDialog(null, "Resultado: " + soma);
    }

}