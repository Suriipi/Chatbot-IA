from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Inicialização do chatbot
chatbot = ChatBot('TravelBot')

# Treinamento do chatbot
trainer = ListTrainer(chatbot)

# Conversas de treinamento
conversations = [
    "Olá!",
    "Olá! Eu sou o seu assistente de viagens. Vamos encontrar o destino perfeito para você! Me conte um pouco sobre seus interesses. Você prefere: A) Praia e Sol B) Cultura e História C) Natureza e Aventura D) Vida Noturna e Entretenimento E) Compras e Gastronomia",

    "A",
    "Ótimo! Com base no seu interesse em Praia e Sol, eu sugiro os seguintes países: Brasil, Tailândia, Havaí. Por favor, escolha um.",
    "Brasil",
    "Excelente escolha! O Brasil tem lindas praias. Aqui estão duas cidades que você deve considerar visitar: Rio de Janeiro e Salvador. O Rio de Janeiro é famoso pelo Cristo Redentor, Pão de Açúcar e belas praias como Copacabana e Ipanema. Salvador é conhecida por suas praias tropicais, o Pelourinho e o Elevador Lacerda.",
    "Tailândia",
    "Excelente escolha! A Tailândia tem praias maravilhosas. Aqui estão duas cidades que você deve considerar visitar: Phuket e Krabi. Phuket é conhecida por suas praias vibrantes e vida noturna. Krabi é famosa por suas paisagens cênicas e ilhas deslumbrantes.",
    "Havaí",
    "Excelente escolha! O Havaí é um paraíso tropical. Aqui estão duas cidades que você deve considerar visitar: Honolulu e Maui. Honolulu é famosa pela Praia de Waikiki e Pearl Harbor. Maui é conhecida por suas praias magníficas e a estrada para Hana.",

    "Rio de Janeiro",
    "Ótima escolha! No Rio de Janeiro, você pode visitar o Cristo Redentor, a Praia de Copacabana, o Pão de Açúcar e o Jardim Botânico. Além disso, você pode aproveitar a vida noturna em Lapa e assistir a um jogo no Maracanã.",
    "Salvador",
    "Ótima escolha! Em Salvador, você pode visitar o Pelourinho, a Igreja de São Francisco, o Mercado Modelo e as praias do Farol da Barra e Itapuã.",
    "Phuket",
    "Ótima escolha! Em Phuket, você pode visitar a Praia de Patong, a Baía de Phang Nga, o Grande Buda e a Cidade Velha de Phuket.",
    "Krabi",
    "Ótima escolha! Em Krabi, você pode visitar a Praia de Railay, as Ilhas Phi Phi, o Templo da Caverna do Tigre e as fontes termais de Klong Thom.",
    "Honolulu",
    "Ótima escolha! Em Honolulu, você pode visitar a Praia de Waikiki, o Memorial de Pearl Harbor, o Parque Diamond Head e o Centro Cultural Polinésio.",
    "Maui",
    "Ótima escolha! Em Maui, você pode visitar a Estrada para Hana, o Parque Nacional Haleakalā, a Praia de Kaanapali e as piscinas de Ohe'o Gulch.",

    "B",
    "Que ótimo! Com base no seu interesse em Cultura e História, eu sugiro os seguintes países: Itália, Japão, Grécia, Egito, México. Por favor, escolha um.",
    "Itália",
    "Excelente escolha! A Itália é rica em cultura e história. Aqui estão duas cidades que você deve considerar visitar: Roma e Florença. Roma é conhecida pelo Coliseu, o Vaticano e a Capela Sistina. Florença é famosa por suas obras de arte e arquitetura, incluindo a Catedral de Santa Maria del Fiore, a Galeria Uffizi e a Ponte Vecchio.",
    "Japão",
    "Excelente escolha! O Japão tem uma rica herança cultural. Aqui estão duas cidades que você deve considerar visitar: Tóquio e Quioto. Tóquio é uma metrópole moderna com templos antigos e mercados vibrantes. Quioto é conhecida por seus templos históricos e belos jardins.",
    "Grécia",
    "Excelente escolha! A Grécia é cheia de história antiga. Aqui estão duas cidades que você deve considerar visitar: Atenas e Santorini. Atenas é famosa pela Acrópole e o Partenon. Santorini é conhecida por suas casas brancas e vistas deslumbrantes do mar.",
    "Egito",
    "Excelente escolha! O Egito é fascinante por sua história antiga. Aqui estão duas cidades que você deve considerar visitar: Cairo e Luxor. Cairo é conhecida pelas Pirâmides de Gizé e o Museu Egípcio. Luxor é famosa pelos templos de Karnak e o Vale dos Reis.",
    "México",
    "Excelente escolha! O México tem uma rica história cultural. Aqui estão duas cidades que você deve considerar visitar: Cidade do México e Chichén Itzá. A Cidade do México é conhecida pelo Zócalo e o Museu Frida Kahlo. Chichén Itzá é famosa por suas ruínas maias.",

    "Roma",
    "Ótima escolha! Em Roma, você pode visitar o Coliseu, o Vaticano, a Fontana di Trevi e o Panteão.",
    "Florença",
    "Ótima escolha! Em Florença, você pode visitar a Catedral de Santa Maria del Fiore, a Galeria Uffizi, a Ponte Vecchio e o Palazzo Pitti.",
    "Tóquio",
    "Ótima escolha! Em Tóquio, você pode visitar o Templo Senso-ji, o Mercado de Peixe de Tsukiji, a Torre de Tóquio e o bairro de Shibuya.",
    "Quioto",
    "Ótima escolha! Em Quioto, você pode visitar o Templo Kinkaku-ji, o Santuário Fushimi Inari, o Bairro de Gion e o Templo Ryoan-ji.",
    "Atenas",
    "Ótima escolha! Em Atenas, você pode visitar a Acrópole, o Museu da Acrópole, o Templo de Zeus Olímpico e o Bairro de Plaka.",
    "Santorini",
    "Ótima escolha! Em Santorini, você pode visitar a Vila de Oia, a Praia Vermelha, o Sítio Arqueológico de Akrotiri e a Caldeira de Santorini.",
    "Cairo",
    "Ótima escolha! Em Cairo, você pode visitar as Pirâmides de Gizé, o Museu Egípcio, a Cidadela de Saladino e o Mercado Khan El Khalili.",
    "Luxor",
    "Ótima escolha! Em Luxor, você pode visitar o Templo de Karnak, o Vale dos Reis, o Templo de Luxor e o Museu de Luxor.",
    "Cidade do México",
    "Ótima escolha! Na Cidade do México, você pode visitar o Zócalo, o Museu Frida Kahlo, o Parque Chapultepec e o Templo Mayor.",
    "Chichén Itzá",
    "Ótima escolha! Em Chichén Itzá, você pode visitar a Pirâmide de Kukulcán, o Templo dos Guerreiros, o Cenote Sagrado e o Campo de Jogos de Bola.",

    "C",
    "Maravilha! Com base no seu interesse em Natureza e Aventura, eu sugiro os seguintes países: Nova Zelândia, Costa Rica, Nepal. Por favor, escolha um.",
    "Nova Zelândia",
    "Excelente escolha! A Nova Zelândia é um paraíso para os amantes da natureza. Aqui estão duas cidades que você deve considerar visitar: Queenstown e Rotorua. Queenstown é conhecida como a capital mundial dos esportes radicais, oferecendo atividades como bungee jumping e skydiving. Rotorua é famosa por suas atividades geotérmicas e cultura Maori.",
    "Costa Rica",
    "Excelente escolha! A Costa Rica é perfeita para aventuras na natureza. Aqui estão duas cidades que você deve considerar visitar: Arenal e Monteverde. Arenal é conhecida pelo Vulcão Arenal e suas fontes termais. Monteverde é famosa por suas florestas nubladas e aventuras de tirolesa.",
    "Nepal",
    "Excelente escolha! O Nepal é ótimo para aventuras ao ar livre. Aqui estão duas cidades que você deve considerar visitar: Katmandu e Pokhara. Katmandu é conhecida por seus templos históricos e cultura vibrante. Pokhara é famosa por suas vistas do Himalaia e trilhas de trekking.",

    "Queenstown",
    "Ótima escolha! Em Queenstown, você pode praticar bungee jumping, skydiving, explorar Milford Sound e fazer trilhas como a Routeburn Track.",
    "Rotorua",
    "Ótima escolha! Em Rotorua, você pode visitar as piscinas de lama, o Parque Kuirau, a Vila Maori de Tamaki e o Vale Waimangu.",
    "Arenal",
    "Ótima escolha! Em Arenal, você pode visitar o Vulcão Arenal, as fontes termais de Tabacón, a Catarata La Fortuna e o Parque Nacional Arenal.",
    "Monteverde",
    "Ótima escolha! Em Monteverde, você pode explorar a Reserva da Floresta Nublada de Monteverde, fazer tirolesa, explorar as pontes suspensas e visitar o Jardim de Borboletas.",
    "Katmandu",
    "Ótima escolha! Em Katmandu, você pode visitar a Praça Durbar, o Templo Swayambhunath (Templo dos Macacos), o Boudhanath Stupa e o Jardim dos Sonhos.",
    "Pokhara",
    "Ótima escolha! Em Pokhara, você pode visitar o Lago Phewa, a Cachoeira Devi, a Caverna Gupteshwor e fazer trekking até o Campo Base do Annapurna.",

    "D",
    "Legal! Com base no seu interesse em Vida Noturna e Entretenimento, eu sugiro os seguintes países: Espanha, Estados Unidos, Brasil. Por favor, escolha um.",
    "Espanha",
    "Excelente escolha! A Espanha tem uma vida noturna vibrante. Aqui estão duas cidades que você deve considerar visitar: Barcelona e Madrid. Barcelona é conhecida por suas discotecas, bares de praia e arquitetura de Gaudí. Madrid oferece uma variedade de clubes noturnos, bares de tapas e eventos culturais.",
    "Estados Unidos",
    "Excelente escolha! Os Estados Unidos têm uma vida noturna incrível. Aqui estão duas cidades que você deve considerar visitar: Nova York e Las Vegas. Nova York é famosa por seus clubes, bares e teatros da Broadway. Las Vegas é conhecida por seus cassinos, shows e vida noturna extravagante.",
    "Brasil",
    "Excelente escolha! O Brasil é famoso por sua vida noturna animada. Aqui estão duas cidades que você deve considerar visitar: São Paulo e Rio de Janeiro. São Paulo tem uma vasta oferta de bares, baladas e eventos culturais. Rio de Janeiro é conhecida pelo Carnaval, sambas e bares na Lapa.",

    "Barcelona",
    "Ótima escolha! Em Barcelona, você pode visitar a Sagrada Família, o Parque Güell, a Casa Batlló e a Praia de Barceloneta. A vida noturna é animada no Bairro Gótico e no Porto Olímpico.",
    "Madrid",
    "Ótima escolha! Em Madrid, você pode visitar o Palácio Real, o Museu do Prado, a Puerta del Sol e o Parque do Retiro. A vida noturna é vibrante nos bairros de Chueca e Malasaña.",
    "Nova York",
    "Ótima escolha! Em Nova York, você pode visitar a Times Square, a Estátua da Liberdade, o Central Park e assistir a um show na Broadway. A vida noturna é animada no Meatpacking District e no East Village.",
    "Las Vegas",
    "Ótima escolha! Em Las Vegas, você pode visitar a Las Vegas Strip, o Bellagio, o Fremont Street Experience e assistir a shows de renome mundial. A vida noturna é vibrante nos cassinos e clubes.",
    "São Paulo",
    "Ótima escolha! Em São Paulo, você pode visitar a Avenida Paulista, o Parque Ibirapuera, o Museu de Arte de São Paulo (MASP) e o Mercado Municipal. A vida noturna é agitada na Vila Madalena e na Rua Augusta.",
    "Rio de Janeiro",
    "Ótima escolha! No Rio de Janeiro, você pode visitar o Cristo Redentor, a Praia de Copacabana, o Pão de Açúcar e o Jardim Botânico. A vida noturna é animada na Lapa e na Barra da Tijuca.",

    "E",
    "Excelente! Com base no seu interesse em Compras e Gastronomia, eu sugiro os seguintes países: França, Emirados Árabes Unidos, Singapura. Por favor, escolha um.",
    "França",
    "Excelente escolha! A França é um destino incrível para compras e gastronomia. Aqui estão duas cidades que você deve considerar visitar: Paris e Lyon. Paris é conhecida por suas lojas de luxo na Champs-Élysées, boutiques no Le Marais e excelentes restaurantes. Lyon é famosa por sua cozinha gourmet e mercados de alimentos.",
    "Emirados Árabes Unidos",
    "Excelente escolha! Os Emirados Árabes Unidos são ótimos para compras e gastronomia. Aqui estão duas cidades que você deve considerar visitar: Dubai e Abu Dhabi. Dubai é famosa por seus shoppings luxuosos e restaurantes de classe mundial. Abu Dhabi oferece uma mistura de lojas de luxo e mercados tradicionais.",
    "Singapura",
    "Excelente escolha! Singapura é perfeita para compras e gastronomia. Aqui estão duas cidades que você deve considerar visitar: Orchard Road e Chinatown. Orchard Road é conhecida por suas lojas de alta moda e grandes centros comerciais. Chinatown oferece uma mistura de lojas tradicionais e restaurantes autênticos.",

    "Paris",
    "Ótima escolha! Em Paris, você pode visitar a Torre Eiffel, o Museu do Louvre, a Catedral de Notre-Dame e fazer compras na Champs-Élysées e no Le Marais.",
    "Lyon",
    "Ótima escolha! Em Lyon, você pode visitar a Basílica de Notre-Dame de Fourvière, o Parque da Tête d'Or, o Museu das Confluências e desfrutar da gastronomia nos Bouchons Lyonnais.",
    "Dubai",
    "Ótima escolha! Em Dubai, você pode visitar o Burj Khalifa, o Dubai Mall, a Palm Jumeirah e o Mercado do Ouro.",
    "Abu Dhabi",
    "Ótima escolha! Em Abu Dhabi, você pode visitar a Grande Mesquita Sheikh Zayed, o Parque da Ferrari World, o Louvre Abu Dhabi e o Mercado Central.",
    "Orchard Road",
    "Ótima escolha! Em Orchard Road, você pode visitar os grandes centros comerciais como o ION Orchard, o Ngee Ann City e o Paragon. Além disso, há muitos restaurantes e cafés incríveis.",
    "Chinatown",
    "Ótima escolha! Em Chinatown, você pode visitar o Templo e Museu da Relíquia do Dente de Buda, o Centro de Comidas de Maxwell, o Bairro Histórico e fazer compras nas lojas tradicionais."
]

trainer.train(conversations)

# Preços médios das passagens de ida e volta de São Paulo
precos_passagens = {
    "Rio de Janeiro": 300,
    "Salvador": 600,
    "Phuket": 5000,
    "Krabi": 5200,
    "Honolulu": 8000,
    "Maui": 8200,
    "Roma": 4000,
    "Florença": 4200,
    "Tóquio": 6000,
    "Quioto": 6200,
    "Atenas": 3500,
    "Santorini": 3700,
    "Cairo": 3200,
    "Luxor": 3400,
    "Cidade do México": 2000,
    "Chichén Itzá": 2200,
    "Queenstown": 7000,
    "Rotorua": 7200,
    "Arenal": 2800,
    "Monteverde": 3000,
    "Katmandu": 6500,
    "Pokhara": 6700,
    "Barcelona": 3800,
    "Madrid": 3600,
    "Nova York": 4200,
    "Las Vegas": 4400,
    "São Paulo": 0,
    "Paris": 4000,
    "Lyon": 4200,
    "Dubai": 5500,
    "Abu Dhabi": 5700,
    "Orchard Road": 4600,
    "Chinatown": 4400
}

# Função para iniciar a conversa com o usuário
def start_chat():
    print("Olá! Eu sou o seu assistente de viagens. Como posso ajudar você hoje?")
    selected_city = None
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ['tchau', 'sair', 'quit', 'exit']:
            print("Bot: Até logo! Boa viagem!")
            break
        elif user_input.lower() == 'voltar':
            print("Bot: Reiniciando a conversa. Como posso ajudar você hoje?")
            start_chat()
            break
        elif user_input.lower() == "qual o preço da passagem?" and selected_city:
            price = precos_passagens.get(selected_city, "Desculpe, não tenho informações sobre essa cidade.")
            print(f"Bot: O preço médio de uma passagem de ida e volta de São Paulo para {selected_city} é de R${price}.")
        else:
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")
            if "Ótima escolha! Em " in response.text:
                selected_city = response.text.split("Ótima escolha! Em ")[1].split(",")[0]

# Iniciar o chatbot
start_chat()
