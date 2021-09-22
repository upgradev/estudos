package capitulo8AcessoArquivosBaseDeDados;

import java.io.BufferedWriter;
import java.io.FileWriter;

import javax.swing.JOptionPane;

public class Exemplo8_1AgendaArquivoSequencial {
    public static void main(String[] args) {
        try {
            String arquivo = EscolherArquivo.caminho();
            BufferedWriter saida;
            saida = new BufferedWriter(new FileWriter(arquivo, true));
            String nome = JOptionPane.showInputDialog("digite o nome");
            nome = nome.toUpperCase();
            String end = JOptionPane.showInputDialog("digite o endereço");
            end = end.toUpperCase();
            String tel = JOptionPane.showInputDialog("Digite o telefone");
            RegAgenda regAg1 = new RegAgenda(nome, end, tel);
            saida.write(regAg1.mostraNome() + "\t");
            saida.write(regAg1.mostraEnd() + "\t");
            saida.write(regAg1.mostraTel() + "\r\t");
            saida.flush();
            saida.close();

        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Erro de acesso ao arquivo");
        }
    }
}