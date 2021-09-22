package capitulo8AcessoArquivosBaseDeDados;

public class RegAgenda {
    private String nome;
    private String end;
    private String tel;

    public RegAgenda(String nome, String end, String tel) {
        this.nome = nome;
        this.end = end;
        this.tel = tel;
    }

    public String mostraNome() {
        return nome;
    }

    public String mostraEnd() {
        return end;
    }

    public String mostraTel() {
        return tel;
    }

}