# https://adventofcode.com/2021/day/16

import sys
import math

trans = { '0':'0000',
          '1':'0001',
          '2':'0010',
          '3':'0011',
          '4':'0100',
          '5':'0101',
          '6':'0110',
          '7':'0111',
          '8':'1000',
          '9':'1001',
          'A':'1010',
          'B':'1011',
          'C':'1100',
          'D':'1101',
          'E':'1110',
          'F':'1111' }

data = ''.join(map(lambda x: trans[x], sys.stdin.read().strip()))

def parse_packet(packet):
    version = int(packet[:3], 2)
    packet = packet[3:]
    type_id = int(packet[:3], 2)
    packet = packet[3:]
    length = 6
    if type_id == 4:
        val = ''
        while True:
            group = packet[:5]
            packet = packet[5:]
            val += group[1:]
            length += 5
            if group[0] == '0':
                break
        return version, length, int(val, 2)
    else:
        length_type_id = packet[0]
        packet = packet[1:]
        length += 1
        sub_versions = []
        sub_values = []
        if length_type_id == '0':
            total_length = int(packet[:15], 2)
            length += 15
            packet = packet[15:]
            sub_packets = packet[:total_length]
            packet = packet[total_length:]
            length += total_length
            while len(sub_packets) > 6:
                ver, l, val = parse_packet(sub_packets)
                sub_versions.append(ver)
                sub_values.append(val)
                sub_packets = sub_packets[l:]
        elif length_type_id == '1':
            num_packets = int(packet[:11], 2)
            packet = packet[11:]
            length += 11
            for _ in range(num_packets):
                ver, l, val = parse_packet(packet)
                sub_versions.append(ver)
                sub_values.append(val)
                packet = packet[l:]
                length += l
        else:
            assert False

        version += sum(sub_versions)
        value = 0
        if type_id == 0:
            value = sum(sub_values)
        elif type_id == 1:
            value = math.prod(sub_values)
        elif type_id == 2:
            value = min(sub_values)
        elif type_id == 3:
            value = max(sub_values)
        elif type_id == 5:
            value = 1 if sub_values[0] > sub_values[1] else 0
        elif type_id == 6:
            value = 1 if sub_values[0] < sub_values[1] else 0
        elif type_id == 7:
            value = 1 if sub_values[0] == sub_values[1] else 0
        else:
            assert False
        return version, length, value

version_sum, _, value = parse_packet(data)
print(version_sum)
print(value)
