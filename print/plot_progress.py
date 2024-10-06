import json
import matplotlib.pyplot as plt

# 读取 JSON 数据
data = []
with open('progress.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

# 提取数据
time_steps = [entry['time_step'] for entry in data]
mean_rewards = [entry['mean reward'] for entry in data]
policy_entropy = [entry['policy_entropy'] for entry in data]
policy_losses = [entry['policy_loss'] for entry in data]
value_losses = [entry['value_loss'] for entry in data]

# 创建并保存 mean reward 图表
plt.figure(figsize=(8, 6))
plt.plot(time_steps, mean_rewards, linestyle='-', color='b')
plt.title('Mean Reward over Time Steps')
plt.xlabel('Time Step')
plt.ylabel('Mean Reward')
plt.tight_layout()
plt.savefig('mean_reward.png')
plt.close()

# 创建并保存 policy entropy 图表
plt.figure(figsize=(8, 6))
plt.plot(time_steps, policy_entropy, linestyle='-', color='y')
plt.title('Policy Entropy over Time Steps')
plt.xlabel('Time Step')
plt.ylabel('Policy Entropy')
plt.tight_layout()
plt.savefig('policy_entropy.png')
plt.close()

# 创建并保存 policy loss 图表
plt.figure(figsize=(8, 6))
plt.plot(time_steps, policy_losses, linestyle='-', color='r')
plt.title('Policy Loss over Time Steps')
plt.xlabel('Time Step')
plt.ylabel('Policy Loss')
plt.tight_layout()
plt.savefig('policy_loss.png')
plt.close()

# 创建并保存 value loss 图表
plt.figure(figsize=(8, 6))
plt.plot(time_steps, value_losses, linestyle='-', color='g')
plt.title('Value Loss over Time Steps')
plt.xlabel('Time Step')
plt.ylabel('Value Loss')
plt.tight_layout()
plt.savefig('value_loss.png')
plt.close()