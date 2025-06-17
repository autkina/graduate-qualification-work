# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- create tables if not
#gauging = измерение		measurement = замер		feature = параметр
import logging

def db_create(cur, conn):
	
	cur.execute('INSERT INTO UserType(name_type) VALUES ("Студент"), ("Научный сотрудник"), ("Администратор");')
	conn.commit()


	cur.execute('CREATE TABLE IF NOT EXISTS UserType ('
		'key_type INT AUTO_INCREMENT PRIMARY KEY,'
		'name_type TEXT NOT NULL);');
	conn.commit()

	cur.execute('CREATE TABLE IF NOT EXISTS BISUser ('
		'key_user INT AUTO_INCREMENT PRIMARY KEY,'
		'login TEXT NOT NULL,'
		'passw INT NOT NULL,'
		'key_type INT NOT NULL,'
		'FOREIGN KEY(key_type) REFERENCES UserType(key_type));');
	conn.commit()

	cur.execute('CREATE TABLE IF NOT EXISTS UserGroup ('
		'key_group INT AUTO_INCREMENT PRIMARY KEY,'
		'key_lect INT NOT NULL,'
		'name_gr TEXT NOT NULL,'
		'isActive boolean NOT NULL,'
		'FOREIGN KEY(key_lect) REFERENCES BISUser(key_user));');
	conn.commit()


	cur.execute('CREATE TABLE IF NOT EXISTS Connect_UserGroup ('
		'key_group INT NOT NULL,'
		'key_user INT NOT NULL,'
		'FOREIGN KEY(key_group) REFERENCES UserGroup(key_group),'
		'FOREIGN KEY(key_user) REFERENCES BISUser(key_user));');
	conn.commit()


	cur.execute('CREATE TABLE IF NOT EXISTS Module ('
		'key_mod INT AUTO_INCREMENT PRIMARY KEY,'
		'key_dev INT NOT NULL,'
		'name_mod TEXT NOT NULL,'
		'descr_mod TEXT,'
		'PDF_mod blob,'
		'isLimitAccess boolean NOT NULL,'
		'FOREIGN KEY(key_dev) REFERENCES BISUser(key_user));');
	conn.commit()


	cur.execute('CREATE TABLE IF NOT EXISTS Connect_GroupModule ('
		'key_group INT NOT NULL,'
		'key_module INT NOT NULL,'
		'isAccessOpened boolean NOT NULL,'
		'FOREIGN KEY(key_group) REFERENCES UserGroup(key_group),'
		'FOREIGN KEY(key_module) REFERENCES Module(key_mod));');
	conn.commit()

	
	cur.execute('CREATE TABLE IF NOT EXISTS Feature ('
		'key_feat INT AUTO_INCREMENT PRIMARY KEY,'
		'name_feat TEXT NOT NULL);');	
	conn.commit()

	# -- почва
	cur.execute('CREATE TABLE IF NOT EXISTS Soil ('
		'key_soil INT AUTO_INCREMENT PRIMARY KEY,'
		'soil_value TEXT NOT NULL);');		
	conn.commit()
	# -- выборка
	cur.execute('CREATE TABLE IF NOT EXISTS Selection ('
		'key_sel INT AUTO_INCREMENT PRIMARY KEY,'
		'name_selection TEXT NOT NULL,'
		'key_soil INT NOT NULL,'
		'date_time datetime NOT NULL,'
		'FOREIGN KEY(key_soil) REFERENCES Soil(key_soil));');
	conn.commit()

	# -- параметры выборки
	cur.execute('CREATE TABLE IF NOT EXISTS SelectionParam ('
		'key_sp INT AUTO_INCREMENT PRIMARY KEY,'
		'key_sel INT NOT NULL,'
		'key_feat INT NOT NULL,'
		'score TEXT NOT NULL,'
		'FOREIGN KEY(key_sel) REFERENCES Selection(key_sel),'
		'FOREIGN KEY(key_feat) REFERENCES Feature(key_feat));');
	conn.commit()

	# -- выборка
	cur.execute('CREATE TABLE IF NOT EXISTS Test_control ('
		'key_tc INT AUTO_INCREMENT PRIMARY KEY,'
		'name_test TEXT NOT NULL,'
		'key_soil INT NOT NULL,'
		'date_time datetime NOT NULL,'
		'FOREIGN KEY(key_soil) REFERENCES Soil(key_soil));');
	conn.commit()

	#-- замер
	cur.execute('CREATE TABLE IF NOT EXISTS Measurement ('
		'key_meas INT AUTO_INCREMENT PRIMARY KEY,'
		'key_module INT NOT NULL,'
		'key_user INT NOT NULL,'
		'key_sel INT NOT NULL,'		
		'name_meas TEXT,'
		'datetime_meas datetime NOT NULL,'
		'FOREIGN KEY(key_module) REFERENCES Module(key_mod),'
		'FOREIGN KEY(key_sel) REFERENCES Selection(key_sel),'
		'FOREIGN KEY(key_user) REFERENCES BISUser(key_user));');
	conn.commit()

	# -- измерение
	cur.execute('CREATE TABLE IF NOT EXISTS Gauging ('
		'key_gaug INT AUTO_INCREMENT PRIMARY KEY,'
		'key_meas INT NOT NULL,'
		'key_feat INT NOT NULL,'
		'score TEXT NOT NULL,'
		'FOREIGN KEY(key_meas) REFERENCES Measurement(key_meas),'
		'FOREIGN KEY(key_feat) REFERENCES Feature(key_feat));');
	
	conn.commit()