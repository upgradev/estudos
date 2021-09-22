package capitulo6EstruturaEstaticaDados;

import javax.swing.JOptionPane;

public class Exemplo6_1 {
    public static void main(String[] args) {
        
        try {
            float[] vetor = new float[10];
            float media, soma = 0;
            String num;
            for(int i = 0; i < vetor.length; i++){
                num = JOptionPane.showInputDialog("Digite o valor " + i + ":");
                vetor[i] = Float.parseFloat(num);
                soma += vetor[i];
            }
            media = soma / vetor.length;
            JOptionPane.showMessageDialog(null, "Média: " + media);

        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Ocorreu um erro durante a leitura ");
        }

    }
}