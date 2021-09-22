package capitulo4EstruturaSelecao;

import javax.swing.JOptionPane;

public class Exemplo4_9 {
    public static void main(String[] args) {
        String codigo;
        codigo = JOptionPane.showInputDialog("Digite o código: ");
        switch (codigo) {
            case "001":
                JOptionPane.showMessageDialog(null, "O produto é caderno");
                break;
            case "002":
                JOptionPane.showMessageDialog(null, "O produto é lápis");
                break;
            case "003":
                JOptionPane.showMessageDialog(null, "O produto é Borracha");
                break;
            default:
                JOptionPane.showMessageDialog(null, "Diverso");
                break;
        }
    }
}