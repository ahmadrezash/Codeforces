def calculate(all_travel, m_ticket_count, one_time_ticket_fee, m_ticket_fee):
	# just one time ticket
	cost1 = all_travel * one_time_ticket_fee
	# multiple tickets
	cost2 = (all_travel // m_ticket_count) * m_ticket_fee
	if all_travel % m_ticket_count != 0:
		# just multiple tickets
		cost2p = cost2 + m_ticket_fee
		# complex case
		cost3 = cost2 + (all_travel % m_ticket_count) * one_time_ticket_fee
		cost = min(cost1, cost2p, cost3)
		return cost

	cost = min(cost1, cost2)
	return cost


# 101 110 1 100

if __name__ == '__main__':
	n, m, a, b = map(int, input().split())
	print(calculate(n, m, a, b))
