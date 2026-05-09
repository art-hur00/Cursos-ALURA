import br.com.alura.screenmatch.modelos.Filme;
import br.com.alura.screenmatch.modelos.Serie;

public class Principal {
    public static void main(String[] args) {
        Filme favorito = new Filme();
        
        favorito.setNome("O poderoso chefão");
        favorito.setAnodeLancamento(1970);
        favorito.setDuracaoEmMinutos(180);

        favorito.exibeFichaTecnica();
        favorito.avalia(9);
        favorito.avalia(8);
        favorito.avalia(9);
        
        System.out.println("Média de avaliações do filme: " + favorito.pegaMedia());
    
        Serie lost = new Serie();
        lost.setNome("Lost");
        lost.setAnodeLancamento(2000);
        lost.exibeFichaTecnica();
        lost.setTemporadas(10);
        lost.setEpisodiosPorTemporada(10);
        lost.setMinutosPorEpisodio(50);
        System.out.println("Duração para maratonar Lost: " + lost.getDuracaoEmMinutos());
    }
}
