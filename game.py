def level_game1():
    valid_words1 = {"siswa", "buku", "kelas"}
    while True:
        print('\n')
        print('**LEVEL I**')
        input_word1 = input('''
+=============+
| S P E B G K |
| I Q F U F E |
| S D I K R L |
| W C D U U A |
| A C D T S S |
+=============+
Temukan 3 kata yang berhubungan dengan SEKOLAH: 
''')
        
        if set(input_word1.replace(' ', '').lower().split(',')) == valid_words1 or set(input_word1.lower().split(' ')) == valid_words1:
            print('Jawaban Anda Benar\n')
            print('========================')
            print('**Silahkan ke Level II**')
            print('========================\n\n')
            break
        else:
            print('Jawaban Anda Salah\nJangan Menyerah. Ayo Coba Lagi!')

def level_game2():
    valid_words2 = {"jogja", "surabaya", "solo", "jakarta", "bandung"}
    while True:
        print('\n')
        print('**LEVEL II**')
        input_word2 = input('''
+====================+
| S J O G J A S O X H|
| U Q F S A W F B H J|
| R P G O K L H A B I|
| A C D L A A J N E B|
| B C G O R S X D O J|
| A F F X T H H U H L|
| Y M K D A N H N N H|
| A H D H N S C G E O|
+====================+
Temukan 5 nama KOTA:  ''')
        
        if set(input_word2.replace(' ', '').lower().split(',')) == valid_words2 or set(input_word2.lower().split(' ')) == valid_words2:
            print('Jawaban Anda Benar\n')
            print('========================')
            print('**Silahkan ke Level III**')
            print('========================\n\n')
            break
        else:
            print('Jawaban Anda Salah\nSemangat. Ayo Coba Lagi!')

def level_game3():
    valid_words3 = {"bali", "jawa", "madura", "lombok", "sulawesi", 'kalimantan', 'bangka'}
    while True:
        print('\n')
        print('**LEVEL III**')
        input_word3 = input('''
+========================+
| S J X G J X S O X K H K|
| B Q F S D W F B H A I Y|
| A P G U K M H T B L B Z|
| N C D L J A W A E I B X|
| G C G A R D X D O M G C|
| K F F W T U H F H A H F|
| A H J E G R F F X N H G|
| J M K S A A H N N T J B|
| B A L I N S C G E A K B|
| J M L O M B O K N N J G|
+========================+
Temukan 7 nama PULAU:  ''')
        
        if set(input_word3.replace(' ', '').lower().split(',')) == valid_words3 or set(input_word3.lower().split(' ')) == valid_words3:
            print('Jawaban Anda Benar\n')
            print('========================')
            print('**Silahkan ke Level IV**')
            print('========================\n\n')
            break
        else:
            print('Jawaban Anda Salah\nTeruslah Mencoba. Jangan Putus Asa!')

def level_game4():
    valid_words4 = {"mangga", "jeruk", 'alpukat', 'sirkaya', 'delima', "apel", "pepaya", "manggis", 'pisang'}
    while True:
        print('\n')
        print('**LEVEL IV**')
        input_word4 = input('''
+===========================+
| Q W E R T Y U I O P A S D |
| M G H J K L Z X C V B D M |
| A L P U K A T K L Z X R V |
| N N M Q W P R T Y U I K S |
| G V B N M E S D F G M S R |
| G Z X C V L N M Q W A R I |
| I U I P P E P I S A N G K |
| S Z J E R U K M Q W G R A |
| Y U I P P A S D P G G J Y |
| L Z X A V D E L I M A R A |
| Y U I Y P A S D S G H J K |
| L Z X A V B N M A W E R T |
| Y U I O P A S D X G H J K |
+===========================+
Temukan 9 nama BUAH:  ''')
        
        if set(input_word4.replace(' ', '').lower().split(',')) == valid_words4 or set(input_word4.lower().split(' ')) == valid_words4:
            print('Jawaban Anda Benar\n')
            print('========================')
            print('**Silahkan ke Level V**')
            print('========================\n\n')
            break
        else:
            print('Jawaban Anda Salah\nJangan Menyerah. Ayo Coba Lagi!')

def level_game5():
    valid_words5 = {"gajah", "kucing", "babi", "bebek", "sapi", "kambing", "badak", "kerbau", 'singa', 'semut', 'anjing'}
    while True:
        print('\n')
        print('**LEVEL V**')
        input_word5 = input('''

+===============================+
| G A J A H X K L M N O P Q R S |
| B K K C f N A U C D E F G H I |
| J K L M U L M C A B C D E F N |
| H I J K L M B I P B E B E K G |
| R S T U V W I N Z A S D P I A |
| X Y Z A B C N K F G A I J K L |
| V B F D G F G E I J P L M U S |
| K V F B S N X R S T I V W C Y |
| B B C D E F G B I J K L M I D |
| A Y S E M U T A T U V A X N Z |
| B B C D E F G U I J K N M G D |
| I K S N A B C D E F G J I J K |
| A B C D E F G H I J K I M N O |
| K Z P X T S N G L M N N P Q R |
| B A D A K S T U V W X G Z A B |
+===============================+
Temukan 11 kata HEWAN:  ''')

        if set(input_word5.replace(' ', '').lower().split(',')) == valid_words5 or set(input_word5.lower().split(' ')) == valid_words5:
            print('Jawaban Anda Benar\nSelamat Anda Telah Menyelesaikan Game ini')
            break
        else:
            print('Jawaban Anda Salah\nDicoba lagi yuk, Pasti Bisa')
            

def play_game():
    while True:
        # Meminta user memasukkan input sesuai nomor 
        level_game = input('''
+==============================================+
|                   Level                      |
+==============================================+
|                 1. Level I                   |                                                        
|                 2. Level II                  |                                                         
|                 3. Level III                 |                                                          
|                 4. Level IV                  |                                                       
|                 5. Level V                   |
+==============================================+                                                         
|///////////////  6. Main Menu  ///////////////|                                     
+==============================================+
Masukkan pilihan level :''')
        
        # Menjalankan fungsi sesuai pilihan menu
        if level_game == '1':
            level_game1()
        elif level_game == '2':
            level_game2()
        elif level_game == '3':
            level_game3()
        elif level_game == '4':
            level_game4()
        elif level_game == '5':
            level_game5()
        elif level_game == '6':
            break
        else:
            print('Pilihan menu yang Anda masukkan tidak tersedia')

# Menu utama daftar nilai siswa
def main_menu():
    while True:
        # Meminta user memasukkan input sesuai nomor 
        menu_game = input('''
+==============================================+
|      Selamat Datang di Game Find My Word     |
+==============================================+
|      1. Play Game                            |   
|      2. Exit                                 |     
+==============================================+
Masukkan pilihan menu : ''')
        
        # Menjalankan fungsi sesuai pilihan menu
        if menu_game == '1':
            play_game()
        elif menu_game == '2':
            break
        else:
            print('Pilihan menu yang Anda masukkan tidak tersedia')

# Menjalankan program utama
main_menu()