package br.com.alura.screenmatch.modelos;

public class Titulo {
    private String nome;
    private int anoDeLancamento;
    private int duracaoEmMinutos;
    private boolean incluidoNoPlano;
    private double somaDasAvaliacoes;
    private int totalDeAvaliacoes;

    public int getTotalDeAvaliações(){
        return totalDeAvaliacoes;
    }
    public void setincluidoNoPlano(boolean  incluidoNoPlano){
        this.incluidoNoPlano = incluidoNoPlano;
    }
    public void setDuracaoEmMinutos(int duracaoEmMinutos){
        this.duracaoEmMinutos = duracaoEmMinutos;
    }
    public void setAnodeLancamento(int anoDeLancamento){
        this.anoDeLancamento = anoDeLancamento;
    }
    


    public int getDuracaoEmMinutos() {
        return duracaoEmMinutos;
    }
    public void exibeFichaTecnica(){
        System.out.println("Nome do filme = " + nome);
        System.out.println("Ano de lançamento = " + anoDeLancamento);
        System.out.println("Duração em minutos: "+duracaoEmMinutos);
        System.out.println("Incluído no plano: "+incluidoNoPlano);
    }
    public void avalia(double nota){
        somaDasAvaliacoes += nota;
        totalDeAvaliacoes ++;
    }
    public double pegaMedia(){
        return somaDasAvaliacoes / totalDeAvaliacoes;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getAnoDelancamento(){
        return anoDeLancamento;
    }
    public String getNome(){
        return nome;
    }
    public boolean isIncluidoNoPlano(){
        return incluidoNoPlano;
    }
}
