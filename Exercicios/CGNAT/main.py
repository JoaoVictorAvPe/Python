def get_port_blocks(output):
    output_list = output.split('\n')

    current_nat = ''
    inform = {}

    for line in output_list:
        if line == '':
            continue

        if ':' not in line and 'default' not in line:
            current_nat = line.replace('Statistics for profile ', '')
            continue

        if 'Total Port Blocks used' in line:
            _, value = line.split(':')
            inform[current_nat] = value.strip()
        
    return inform


def get_max_subscribers(output):
    return [
        line.replace('max-subscribers', '').strip() 
        for line in output.split('\n') 
        if 'max-subscribers' in line
    ][0]

output_port_blocks = '''
Statistics for profile default
Total number of subscribers : 0
Port Blocks per IP : 64512
Max Public IPs : 1
Total Reserved IPs : 0
Total Used IPs : 0

Statistics for profile default
Total number of subscribers : 0
Port Blocks per IP : 1008
Max Public IPs : 1
Total Reserved IPs : 0
Total Used IPs : 0

Statistics for profile nat-SPO-01
Total number of subscribers : 559
Port Blocks per IP : 63
Max Public IPs : 61
Total Reserved IPs : 61
Total Used IPs : 51
Pool group name : cgnat-group-SPO-01
Total Public IPs in pool : 64
Total Public IPs reserved : 61
Total Public IPs used : 51
Total Public IPs used high value : 56
Total Port Blocks in pool : 3843
 Total Port Blocks used                      : 559

Statistics for profile nat-SPO-SKY01
Total number of subscribers : 5100
Port Blocks per IP : 126
Max Public IPs : 66
Total Reserved IPs : 66
Total Used IPs : 66
Pool group name : cgnat-group-SPO-SKY01
Total Public IPs in pool : 72
Total Public IPs reserved : 66
Total Public IPs used : 66
Total Public IPs used high value : 66
Total Port Blocks in pool : 8316
 Total Port Blocks used                      : 5100
'''

output_max_subscribers = '''
 bng nat profile named nat-BSA-01
 max-subscribers 4096
block-size 512 blocks 3
ip pool cgnat-group-BSA-01
ip alloc-type hybrid
ip reserved-blocks 63
subscribers-per-ip 63
!
bng nat profile named nat-BSA-SKY01
 max-subscribers 1024
block-size 256 blocks 4
ip pool cgnat-group-BSA-SKY01
ip alloc-type hybrid
ip reserved-blocks 126
subscribers-per-ip 126
!
'''

lista = []
with open('Exercicios/CGNAT/max_subscribers.txt', 'r') as arquivo:
    lista = arquivo.readlines()


def get_max_sub(lista):
    current_nat = ''
    inform = {}

    for line in lista:
        if line == '!\n':
            continue

        if 'bng nat profile named' in line:
            current_nat = line.replace('bng nat profile named', '').strip()
            continue

        if 'max-subscribers' in line:
            inform[current_nat] = line.replace('max-subscribers', '').strip()

    inform.pop('') 
    return inform

print(get_max_sub(lista))





