-- 0-uniq_users.sql We are all unique! - This will create a table of users
-- script can be exeecuted on any db
CREATE TABLE If NOT EXISTS `users` (  
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255)
);
