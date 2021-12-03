1. ``cd`` - это команда оболочки sh, bash. Т.к. работа происходит внутри оболочки, например bash, то и изменениядиректорий и окружения должны происходить внутренними командами самой оболочки, а не вызываться внешними программами.   
2. ``grep <some_string> <some_file> -c``  
3. ``systemd``  
4. ``ls 2> /dev/pts/2``  
5. ``cat ./linux2/README.md | grep ls > test.md``  
6. Да, можно передать. ``echo 123 >/dev/tty1``. В консоле виртуальноый машины можно будет увидеть отправленный текс.  
7. ``bash 5>&1`` - создается файловый дескриптор и перенаправляется в stdout.   
``echo netology > /proc/$$/fd/5`` - произойдет вывод на экран данных отправленных в файлоый дискриптор. Это произойдет из-зп того, что предыдущей командой мы указали перенаправлять все данные в stdout  
8. Получится, если использовать промежуточный файловый дескриптор. ``ls -d /root ./file1 ./non-existent_file 3>&1 1>&2 2>&3 | grep "exist"``  
9. ``cat /proc/$$/environ`` отображает переменные окружения. Можно отобразить через ``env``, ``printenv``, ``(set -o posix; set)``  
10. ``proc/<PID>/cmdline`` содержит команду с помощью которой был запущен процесс, а также переданные ей параметры, если в этом файле  ничего нет, то процесс является зомби.  
``/proc/<PID>/exe`` символическая ссылка на исполняемый файл. В многопоточном процессе содержимое этой символической ссылки может быть не доступно, если основной поток уже завершается.  
11. ``sse4_2``
12. По умолчанию при выполнении команды на удаленной машине с использованием ssh для удаленного сеанса не выделяется TTY. Для изменения этого положения необходимо принудительно выделить TTY с помощью флага -t ``ssh -t localhost 'tty'`` 
13. ``ping localhost  
ctrl+d  
ps -a | grep ping  
screen -S test  
reptyr -s <PID> ``  
14. ``tee`` используется для записи вывыода команды в файл. ``echo`` используется длы вывода передаваемой строки. Следовательно при использовании ``sudo echo`` права root используются только для вывода на экран строки, но не дают права на запись в файл, а при использовании ``echo string | sudo tee /root/new_file`` вывод из команды ``echo`` передается команде ``tee`` с правами root