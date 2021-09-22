package capitulo6EstruturaEstaticaDados;

import javax.swing.JOptionPane;

public class Exemplo6_2 {
    public static void main(String[] args) {

        int[] test1 = new int[10];
        int[] test2 = new int[10];
        String num;

        try {
            for (int i = 0; i < test1.length; i++) {
                num = JOptionPane.showInputDialog("Digite o valor " + i + ":");
                test1[i] = Integer.parseInt(num);
            }
            for (int i = 0; i < test1.length; i++) {
                if (i % 2 == 0) {
                    test2[i] = test1[i] * 5;
                } else {
                    test2[i] = test1[i] + 5;
                }
            }
            System.out.printf("%s\n", "Resultado");
            for (int i = 0; i < 10; i++) {
                System.out.printf("%s%d%s%d", "teste1[", i, "]=", test1[i]);
                System.out.printf("%10s%d%s%d\n", "teste2[", i, "]=", test2[i]);
            }
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Ocorreu um erro durante a leitura ");
        }

    }
}