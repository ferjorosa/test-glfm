function x = f_g(y, mu, w)
    % transformation function for real-valued data
    % Y -> X (from pseudo-obversations to data)
    if (w == 0)
        error('scaling factor should never be 0');
    end
    x = y./w + mu;
end