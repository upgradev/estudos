package capitulo6EstruturaEstaticaDados;

import javax.swing.JOptionPane;

public class Exemplo6_4MediaTemperatura {
    public static void main(String[] args) {
        final int diasSemanas = 7;
        float[] temperatura = new float[diasSemanas];
        float soma = 0f, media;

        try {
            temperatura[0] = 19.0f;
            temperatura[1] = 23.0f;
            temperatura[2] = 21.0f;
            temperatura[3] = 25.0f;
            temperatura[4] = 22.0f;
            temperatura[5] = 20.0f;
            temperatura[6] = 24.0f;
            for (int i = 0; i < diasSemanas; i++) {
                soma += temperatura[i];
            }
            media = soma / diasSemanas;
            JOptionPane.showMessageDialog(null, "Média da semana " + media);

        } catch (Exception e) {
            // TODO: handle exception
        }
    }
}