function x = f_p(y, mu, w)
    % transformation function for positive data
    % Y -> X (from pseudo-obversations to data)
    if (w == 0)
        error('scaling factor should never be 0');
    end
    x = log( exp(y) + 1 )./w + mu;
end