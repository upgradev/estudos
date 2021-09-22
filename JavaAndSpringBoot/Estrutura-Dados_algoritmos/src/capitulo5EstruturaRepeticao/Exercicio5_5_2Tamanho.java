package capitulo5EstruturaRepeticao;

import javax.swing.JOptionPane;

public class Exercicio5_5_2Tamanho {
    public static void main(String[] args) {
        float pedro, lucas;
        int anos = 0;
        pedro = 1.50f;
        lucas = 1.10f;
        while (lucas != pedro){
            pedro += 0.02f;
            lucas += 0.03f;
            anos++;
        }
        JOptionPane.showMessageDialog(null, "Total de anos para terem o mesmo tamanho é: "+ anos);
    }    
}