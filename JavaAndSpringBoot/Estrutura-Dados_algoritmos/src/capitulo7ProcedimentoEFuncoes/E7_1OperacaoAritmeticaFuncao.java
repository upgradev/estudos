package capitulo7ProcedimentoEFuncoes;

import javax.swing.JOptionPane;

public class E7_1OperacaoAritmeticaFuncao {
    public static void main(String[] args) {

        int opcao;
        opcao = Integer.parseInt(JOptionPane.showInputDialog(
                "Escola uma opcção: \n" + "1 - Adição " + "2 - Subtração " + "3 - Multiplicação " + "4 - Divisão "));

        switch (opcao) {
            case 1:
                modAdicao();
                break;
            case 2:
                modSubtracao();
                break;
            case 3:
                modMultiplicacao();
                break;
            case 4:
                modDivisao();
                break;

            default:
                break;
        }
    }

    static void modAdicao() {
        double v1;
        double v2;
        double res;
        v1 = Double.parseDouble(JOptionPane.showInputDialog("Digite o primeiro valor: "));
        v2 = Double.parseDouble(JOptionPane.showInputDialog("Digite o segundo valor: "));
        res = v1 + v2;
        JOptionPane.showMessageDialog(null, "Resultado da soma: " + res);
    }

    static void modSubtracao() {
        double v1;
        double v2;
        double res;
        v1 = Double.parseDouble(JOptionPane.showInputDialog("Digite o primeiro valor: "));
        v2 = Double.parseDouble(JOptionPane.showInputDialog("Digite o segundo valor: "));
        res = v1 - v2;
        JOptionPane.showMessageDialog(null, "Resultado da Subtr: " + res);
    }

    static void modMultiplicacao() {
        double v1;
        double v2;
        double res;
        v1 = Double.parseDouble(JOptionPane.showInputDialog("Digite o primeiro valor: "));
        v2 = Double.parseDouble(JOptionPane.showInputDialog("Digite o segundo valor: "));
        res = v1 * v2;
        JOptionPane.showMessageDialog(null, "Resultado da Multipl: " + res);
    }

    static void modDivisao() {
        double v1;
        double v2;
        double res;
        v1 = Double.parseDouble(JOptionPane.showInputDialog("Digite o primeiro valor: "));
        v2 = Double.parseDouble(JOptionPane.showInputDialog("Digite o segundo valor: "));
        res = v1 / v2;
        JOptionPane.showMessageDialog(null, "Resultado da Div: " + res);
    }
}