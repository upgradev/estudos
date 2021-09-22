package capitulo4EstruturaSelecao;

import javax.swing.JOptionPane;

public class Exemplo4_5 {

    public static void main(String[] args) {

        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Número: "));
        if (numero % 2 == 1) {
            JOptionPane.showMessageDialog(null, "O número é impar ");
        }

    }

}