package capitulo9Recursividade;

import javax.swing.JOptionPane;

public class Exemplo9_1Fatorial {

    static int fatorial(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * fatorial(n - 1);
        }
    }

    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite um número maior do que zero: "));
        JOptionPane.showMessageDialog(null, "O fatorial de " + numero + " é " + fatorial(numero));
    }

}