package capitulo7ProcedimentoEFuncoes;

import javax.swing.JOptionPane;

public class E7_2Fatorial {
    public static void main(String[] args) {
        int numero;
        int fat;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Qual o número: "));
        fat = fatorial(numero);
        JOptionPane.showMessageDialog(null, "Fatorial de " + numero + " é " + fat);
    }

    static int fatorial(int numero) {
        int f = 1;
        for (int i = 1; i <= numero; i++) {
            f = f * i;
        }
        return f;
    }
}