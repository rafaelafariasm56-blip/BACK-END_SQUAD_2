from django.core.management.base import BaseCommand
from blog.models import Category, Author, BlogPost
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Populate the database with sample blog data'

    def handle(self, *args, **options):
        self.stdout.write('Populating blog data...')
        
        categories_data = [
            'Cães', 'Gatos', 'Alimentação', 'Pássaros'
        ]
        
        categories = {}
        for cat_name in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_name,
                defaults={'slug': slugify(cat_name)}
            )
            categories[cat_name] = category
            if created:
                self.stdout.write(f'Created category: {cat_name}')

        authors_data = [
            {'name': 'Dra. Ana Sousa', 'email': 'ana@animalisecare.com'},
            {'name': 'Dr. Carlos Andrade', 'email': 'carlos@animalisecare.com'},
            {'name': 'Dra. Mariana Silva', 'email': 'mariana@animalisecare.com'},
            {'name': 'Dra. Fernanda Costa', 'email': 'fernanda@animalisecare.com'},
            {'name': 'Dra. Camila Nunes', 'email': 'camila@animalisecare.com'},
            {'name': 'Dr. Paulo Meireles', 'email': 'paulo@animalisecare.com'},
            {'name': 'Dra. Aline Santos', 'email': 'aline@animalisecare.com'},
            {'name': 'Dra. Juliana Prado', 'email': 'juliana@animalisecare.com'},
            {'name': 'Dr. Ricardo Lima', 'email': 'ricardo@animalisecare.com'},
        ]
        
        authors = {}
        for author_data in authors_data:
            author, created = Author.objects.get_or_create(
                name=author_data['name'],
                defaults={'email': author_data['email']}
            )
            authors[author_data['name']] = author
            if created:
                self.stdout.write(f'Created author: {author_data["name"]}')

        posts_data = [
            {
                'title': '5 Sinais de que o seu Cão pode estar com Dor',
                'author': 'Dra. Ana Sousa',
                'image': 'https://www.petz.com.br/blog/wp-content/uploads/2018/11/como-saber-se-o-cao-esta-com-dor.jpg',
                'category': 'Cães',
                'featured': True,
                'content': '<p>A dor em cães pode ser subtil. Fique atento a mudanças de comportamento como falta de apetite, relutância em se mover ou agressividade incomum. Identificar cedo é crucial para o bem-estar do seu amigo.</p><p>Se notar algum destes sinais, não hesite em procurar um veterinário. Um diagnóstico preciso pode fazer toda a diferença no tratamento e na qualidade de vida do seu pet.</p>'
            },
            {
                'title': 'A importância da Vacinação para Gatos',
                'author': 'Dr. Carlos Andrade',
                'image': 'https://www.petz.com.br/blog/wp-content/uploads/2016/10/vacinacao-para-gatos-1280x720.jpg',
                'category': 'Gatos',
                'featured': True,
                'content': '<p>Manter a vacinação do seu gato em dia é um ato de amor e responsabilidade. As vacinas protegem contra doenças graves e contagiosas. Converse com seu veterinário para criar um calendário de vacinação adequado para o estilo de vida do seu felino.</p>'
            },
            {
                'title': 'Alimentação Natural: Prós e Contras',
                'author': 'Dra. Ana Sousa',
                'image': 'https://jpimg.com.br/uploads/2025/03/veja-os-beneficios-da-racao-e-da-alimentacao-natural-para-pets.jpg',
                'category': 'Alimentação',
                'featured': False,
                'content': '<p>A alimentação natural tem ganhado popularidade, mas é preciso cuidado. Os prós incluem ingredientes frescos e sem conservantes. Os contras envolvem o risco de desbalanceamento nutricional. Consulte sempre um veterinário nutricionista antes de mudar a dieta do seu pet.</p>'
            },
            {
                'title': 'Arranhadores: Por que todo Gato Precisa de Um',
                'author': 'Dr. Carlos Andrade',
                'image': 'https://blog-static.petlove.com.br/wp-content/uploads/2021/02/Gato-arranhador-Petlove.jpg',
                'category': 'Gatos',
                'featured': True,
                'content': '<p>Arranhar é um comportamento natural dos gatos. Ajuda a afiar as unhas e a marcar território. Oferecer um arranhador adequado evita que seus móveis se tornem o alvo principal. Existem diversos modelos, descubra qual o seu gato prefere!</p>'
            },
            {
                'title': 'Alimentação Natural: Benefícios para Cães',
                'author': 'Dra. Mariana Silva',
                'image': 'https://media.gazetadopovo.com.br/2024/05/02134321/Shutterstock_2310822195-960x540.jpg',
                'category': 'Cães',
                'featured': True,
                'content': '<p>A alimentação natural pode trazer mais saúde e disposição para os cães, evitando conservantes e ingredientes artificiais. É importante contar com a orientação de um veterinário para montar a dieta adequada.</p>'
            },
            {
                'title': 'Como Evitar Bolas de Pelo em Gatos',
                'author': 'Dr. Carlos Andrade',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSILNNgitLym95ob69K3yyII3n-nhIyB9efMg&s',
                'category': 'Gatos',
                'featured': False,
                'content': '<p>Escovar o gato regularmente ajuda a reduzir a formação de bolas de pelo. Além disso, rações específicas e o uso de petiscos com fibras auxiliam no trato intestinal.</p>'
            },
            {
                'title': 'Cachorros Podem Comer Frutas?',
                'author': 'Dra. Fernanda Costa',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsisvT2rwbITooSQBioEgt2LyN8SUsNDDFSA&s',
                'category': 'Cães',
                'featured': False,
                'content': '<p>Algumas frutas como maçã, banana e melancia são liberadas para cães. Já uvas e abacate devem ser evitados. Sempre ofereça sem sementes e em pequenas quantidades.</p>'
            },
            {
                'title': 'Como Ensinar o Cachorro a Fazer as Necessidades no Lugar Certo',
                'author': 'Dra. Camila Nunes',
                'image': 'https://blog-static.petlove.com.br/wp-content/uploads/2012/10/Cachorro-no-tapete-higienico.jpg',
                'category': 'Cães',
                'featured': False,
                'content': '<p>O adestramento positivo, paciência e o uso de tapetes higiênicos são fundamentais para ensinar o pet. Recompensas como petiscos aceleram o aprendizado.</p>'
            },
            {
                'title': 'Brinquedos Interativos para Entreter seu Gato',
                'author': 'Dr. Paulo Meireles',
                'image': 'https://blog-static.petlove.com.br/wp-content/uploads/2021/10/brinquedos-barato-gatos-Petlove.jpg',
                'category': 'Gatos',
                'featured': False,
                'content': '<p>Brinquedos que estimulam a caça e o movimento são essenciais para o bem-estar felino. Bolinhas, varinhas com penas e brinquedos com catnip fazem sucesso.</p>'
            },
            {
                'title': 'Vacinação de Cães: Quais São as Principais?',
                'author': 'Dra. Aline Santos',
                'image': 'https://optimumpet.com.br/media/uploads/2022/12/vacinas-para-caes-scaled.webp',
                'category': 'Cães',
                'featured': True,
                'content': '<p>Vacinas como V8, V10, antirrábica e a de gripe canina são essenciais para a saúde e proteção dos cães. Manter a carteirinha em dia é fundamental.</p>'
            },
            {
                'title': 'Areia de Gato: Qual a Melhor Opção?',
                'author': 'Dra. Juliana Prado',
                'image': 'https://opinioescertificadas.com.br/wp-content/uploads/2021/02/melhor-areia-para-gatos.jpg',
                'category': 'Gatos',
                'featured': False,
                'content': '<p>Existem areias de sílica, granulado de madeira e argila. Cada uma tem vantagens, como maior absorção ou neutralização de odores. A escolha depende do perfil do tutor e do gato.</p>'
            },
            {
                'title': 'Como Cuidar de Pássaros em Casa',
                'author': 'Dr. Ricardo Lima',
                'image': 'https://www.petz.com.br/blog/wp-content/uploads/2017/06/aves-domesticas.jpg',
                'category': 'Pássaros',
                'featured': False,
                'content': '<p>Pássaros precisam de gaiolas espaçosas, alimentação variada e estímulos como poleiros e brinquedos. Atenção à higiene é indispensável para evitar doenças.</p>'
            },
            {
                'title': 'Banho em Cães: Com Que Frequência Dar?',
                'author': 'Dra. Mariana Silva',
                'image': 'https://www.petz.com.br/blog/wp-content/uploads/2020/05/cao-pode-tomar-banho-todo-dia-1280x720.jpg',
                'category': 'Cães',
                'featured': False,
                'content': '<p>A frequência do banho varia conforme a raça e o tipo de pelo. Em média, de 15 em 15 dias é o recomendado. Uso de shampoos específicos é essencial.</p>'
            },
            {
                'title': 'Gatos Podem Tomar Banho?',
                'author': 'Dr. Carlos Andrade',
                'image': 'https://www.petz.com.br/blog/wp-content/uploads/2019/05/gato-toma-banho-1.jpg',
                'category': 'Gatos',
                'featured': False,
                'content': '<p>Em geral, gatos não precisam de banho, pois se higienizam lambendo-se. Porém, em casos específicos de sujeira ou problemas de saúde, o banho pode ser necessário.</p>'
            },
            {
                'title': 'Adestramento Positivo: Como Funciona?',
                'author': 'Dra. Fernanda Costa',
                'image': 'https://www.petz.com.br/blog/wp-content/uploads/2020/05/reforco-positivo.jpg',
                'category': 'Cães',
                'featured': True,
                'content': '<p>O adestramento positivo é baseado em recompensas ao invés de punições. Ensina o cão de forma eficaz e fortalece o vínculo com o tutor.</p>'
            },
            {
                'title': 'O que Significa o Ronronar dos Gatos?',
                'author': 'Dra. Camila Nunes',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCrovA-cgNo1Ytx0ETDjoItQ4pkSZZ6G0BKQ&s',
                'category': 'Gatos',
                'featured': False,
                'content': '<p>O ronronar é um sinal de bem-estar, mas também pode indicar ansiedade ou dor. Observar o contexto do comportamento é essencial para entender seu gato.</p>'
            },
            {
                'title': 'Exercícios para Cães em Apartamento',
                'author': 'Dr. Paulo Meireles',
                'image': 'https://blog-static.petlove.com.br/wp-content/uploads/2020/09/Cachorro-exercicio-Petlove.jpg',
                'category': 'Cães',
                'featured': False,
                'content': '<p>Mesmo em apartamentos, cães precisam se exercitar. Brincadeiras com bolinha, passeios diários e circuitos dentro de casa ajudam na saúde física e mental.</p>'
            }
        ]

        for post_data in posts_data:
            author = authors[post_data['author']]
            category = categories[post_data['category']]
            
            blog_post, created = BlogPost.objects.get_or_create(
                title=post_data['title'],
                defaults={
                    'slug': slugify(post_data['title']),
                    'author': author,
                    'category': category,
                    'content': post_data['content'],
                    'image': post_data['image'],
                    'featured': post_data['featured'],
                    'published': True
                }
            )
            
            if created:
                self.stdout.write(f'Created post: {post_data["title"]}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated blog data!')
        )
