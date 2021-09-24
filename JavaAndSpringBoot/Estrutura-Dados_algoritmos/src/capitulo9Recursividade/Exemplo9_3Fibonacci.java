package capitulo9Recursividade;

import javax.swing.JOptionPane;

public class Exemplo9_3Fibonacci {
    public static void main(String[] args) {

        long numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite o n-esimo elemento"));
        JOptionPane.showMessageDialog(null,
                "O " + numero + " º elemento da sequencia é: " + fibonacciNaoRecursiva(numero));
        JOptionPane.showMessageDialog(null,
                "O " + numero + " º elemento da sequencia é: " + fibonacciRecursiva(numero));

    }

    public static long fibonacciNaoRecursiva(long n) {
        long ultimo, i, penultimo, seguinte;
        ultimo = 1;
        penultimo = 0;
        i = 3;
        if (n == 1)
            return 0;
        if (n == 2)
            return 1;
        while (n >= i) {
            seguinte = ultimo + penultimo;
            penultimo = ultimo;
            ultimo = seguinte;
            i++;
        }
        return ultimo;
    }

    public static long fibonacciRecursiva(long n) {
        long num = 0;
        if (n == 1)
            return 0;
        else if (n == 2)
            return 1;
        else if (n >= 3) {
            num = fibonacciRecursiva(n - 1) + fibonacciRecursiva(n - 2);
        }
        return num;
    }
}