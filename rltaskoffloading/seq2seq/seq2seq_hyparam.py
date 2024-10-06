import tensorflow as tf

# 循环神经网络（RNN）定义超参数，特别是 LSTM（长短期记忆网络）模型
def get_hparams():
    '''
    hparams = tf.contrib.training.HParams(
        unit_type="lstm",
        num_units=256,
        learning_rate=0.0005,
        n_features=5,
        time_major=True,
        is_attention=True,
        forget_bias=1.0,
        dropout=0.2,
        num_gpus=1,
        num_layers=4,
        num_residual_layers=0,
        is_greedy=False,
        start_token=3,
        end_token=4,
        is_bidencoder=True,
        max_gradient_norm = 5.0
    )
    '''

    #modify the num_units
    hparams = tf.contrib.training.HParams(
        unit_type="layer_norm_lstm",
        num_units=256,
        learning_rate=0.00005,
        supervised_learning_rate = 0.00005,
        n_features=5,
        time_major=True,
        is_attention=True,
        forget_bias=1.0,
        dropout=0,
        num_gpus=1,
        num_layers=2,
        num_residual_layers=0,
        is_greedy=False,
        inference_model="sample",
        start_token=0,
        end_token=5,
        is_bidencoder=True
    )

    return hparams

# 定义值网络（用于强化学习中的状态价值评估）的超参数
# hyper-parameters for value networks
def get_value_network_hparams():
    hparams = tf.contrib.training.HParams(
    unit_type="layer_norm_lstm",
    num_units=128,
    learning_rate=0.0001,
    n_features=3,
    time_major=True,
    is_attention=True,
    forget_bias=1.0,
    dropout=0,
    num_gpus=1,
    num_layers=2,
    num_residual_layers=0,
    is_greedy=False,
    inference_model="sample",
    start_token=0,
    end_token=3,
    is_bidencoder=True
    )

    return hparams

# 为计算成本模型定义超参数，这可能涉及在序列模型上评估某些开销或成本函数
def get_cost_hparams():
    hparams = tf.contrib.training.HParams(
        unit_type="layer_norm_lstm",
        learning_rate=0.0001,
        n_features=5,
        time_major=False,
        is_attention=False,
        is_bidencoder=True,
        attention_out_put_unit_size=512,
        num_units = 512,
        forget_bias=1.0,
        connected_layer_unit=512,
        dropout=0.2,
        num_gpus=1,
        num_layers=4,
        num_residual_layers=0,
        start_token=4,
        end_token=5,
    )

    return hparams

# 为卷积神经网络（CNN）的成本模型定义超参数
def get_cnn_cost_hparams():
    hparams = tf.contrib.training.HParams(
        learning_rate=0.001,
        batch_size=128,
        first_filter_size=32,
        second_filter_size=32,
        kernel_size=[5, 5],
        pool_size=[2, 2],
        num_layers=4,
        num_residual_layers=0,
        time_major=False,
        connected_hidden_layer_size=1024,
        n_features=5,
        unit_type = "layer_norm_lstm",
        num_units = 512,
        forget_bias = 1.0,
        dropout = 0.2,
        num_gpus = 1
    )

    return hparams