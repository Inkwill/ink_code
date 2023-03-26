#! /usr/bin/lua

-- Usage: mysql2sqlite.lua [data base name]
-- 			$ ./mysql2sqlite.lua my_database
-- 			$ ./mysql2sqlite.lua "my_database my_table"
-- 			$ ./mysql2sqlite

-- Set here the path to the temp file you want mysqldump to dump the database into
local mysqldump_file = 'time.sql'

-- Set here your MySQL default database name and MySQL credentials
local dbName = arg[1] and arg[1] or 'world'
local dbUser, dbPw = 'root', 'artemis'

-- Various variable initialisation
local fh, line, tableName, indexName, indexKey, findUs, replaceBy
local previous, keys = nil, {}

-- Extracts database from MySQL, remove <--no-data> if you want to extract all INSERT's
os.execute('mysqldump --compatible=ansi --no-data --skip-extended-insert --compact -u '..dbUser..' -p'..dbPw..' '..dbName..' > '..mysqldump_file)

fh, err = io.open(mysqldump_file, 'r')
if not fh then return print(err) end

for line in fh:lines() do
	-- skip comments
	if not line:find('^/%*') then
		-- Print all INSERT's replacing `5 o\'clock` by the sqlite escape format: `5 o''clock`, then loop.
		if line:find('^INSERT', 1) then
			if line:find("\\'") then line = line:gsub("\\'", "''") end
			print(line)
		else
			-- Remove the KEY declaration from the create block except for the PRIMARY KEY and store it in table for later use
			-- then loop
			if line:find('^  KEY') or line:find('^  UNIQUE KEY') or line:find('^  FULLTEXT KEY') and not line:find('PRIMARY') then
				indexName = line:match('"([^"]+)')
				indexKey = line:match('%("([^"]+)')
				table.insert(keys, 'CREATE INDEX "'..tableName..'_'..indexName..'" ON "'..tableName..'"("'..indexKey..'");')

			else
				-- Stores table name in variable
				if line:find('CREATE', 1, true) then
					tableName = line:match('"([^"]+)', 1)
				end

				if line:find(');', 1, true) then
					previous = previous:gsub(',$', '',1)
					print(previous, '\n);')
					previous = nil
				else
					if previous then print(previous) end
					-- Various replacements of MySQL specifics
					findUs = {
						'AUTO_INCREMENT','auto_increment',
						'CHARACTER SET [^ ]+ ','character set [^ ]+ ',
						'DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP', 'default current_timestamp on update current_timestamp',
						'COLLATE [^ ]+','collate [^]+',
						'UNSIGNED','unsigned',
						'ENUM[^)]+%)', 'enum[^)]+%)',
						'SET%([^)]+%)', 'set%([^)]+%)'
					}
					replaceBy  = { '', '', '', '', '',  '', '', '', '', '', 'text', 'text','text', 'text'}
					for k, findMe in pairs(findUs) do
						line = line:gsub(findMe, replaceBy[k])
					end
					previous = line
				end
			end
		end
	end
end
fh:close()

for k, v in pairs(keys) do
	print(v)
end
