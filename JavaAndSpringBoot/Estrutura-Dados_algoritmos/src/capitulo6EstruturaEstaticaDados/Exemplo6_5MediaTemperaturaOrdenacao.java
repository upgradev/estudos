package capitulo6EstruturaEstaticaDados;

import java.text.DecimalFormat;

import javax.swing.JOptionPane;

public class Exemplo6_5MediaTemperaturaOrdenacao {
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
            float x;
            DecimalFormat formatter = new DecimalFormat("#.00");
            for (int i = 0; i < diasSemanas; i++) {
                soma += temperatura[i];
                for (int j = i + 1; j < diasSemanas; j++) {
                    if (temperatura[j] < temperatura[i]) {
                        x = temperatura[i];
                        temperatura[i] = temperatura[j];
                        temperatura[j] = x;
                    }
                }
            }
            media = soma / diasSemanas;
            JOptionPane.showMessageDialog(null, "Média da semana " + formatter.format(media));
            JOptionPane.showMessageDialog(null, "Mínima da semana " + temperatura[0]);
            JOptionPane.showMessageDialog(null, "Máxima da semana " + temperatura[6]);

        } catch (Exception e) {
            // TODO: handle exception
        }
    }
}