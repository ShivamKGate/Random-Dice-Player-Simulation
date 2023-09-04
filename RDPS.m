P1 = input("Enter Player 1 name: ", "s");
P2 = input("Enter Player 2 name: ", "s");
n = input("The number of attempts n = ");
Score1 = 0;
Score2 = 0;
P1_dice = 0;
P2_dice = 0;
Driver_name ="";
Follower_name ="";
for round = 1:(n+1)
    if round == 1
        while true
            P1_dice = randi([1, 6], 1);
            P2_dice = randi([1, 6], 1);
            if P1_dice ~= P2_dice
                break;
            end
        end 
        if P1_dice > P2_dice
            driver = P1_dice;
            Driver_name = P1;
            Follower_name = P2;
        else
            driver = P2_dice;
            Driver_name = P2;
            Follower_name = P1;
        end
        fprintf('The Driver is %s, the Follower is %s \n', Driver_name, Follower_name);
    else
        follower_roll = randi([1,6],1);
        driver_roll = randi([1,6],1);
        if driver_roll == follower_roll
            Score2 = Score2 + 1; 
            fprintf('The winner of round %i is %s \n',(round-1),Follower_name);
        else
            Score1 = Score1 + 1; 
            fprintf('The winner of round %i is %s \n',(round-1),Driver_name);
        end
    end
end
if Score1 == Score2
    fprintf('The game is a tie!\n');
elseif Score1 > Score2
    fprintf('The winner of the game is %s \n', string(Driver_name));
else
    fprintf('The winner of the game is %s \n', string(Follower_name));
end
fprintf('The points for %s is %d.\n', Follower_name,Score2);
fprintf('The points for %s is %d.\n', Driver_name,Score1);
