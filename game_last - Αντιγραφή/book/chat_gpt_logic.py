# https://platform.openai.com/account/usage
# https://www.youtube.com/watch?v=DMZqli5jgMw
# https://www.youtube.com/results?search_query=chat+gpt3+api
# https://learndataanalysis.org/getting-started-with-openai-gpt-gpt-3-5-model-api-in-python/

import openai

class Logic:
    def __init__(self, gpt_role = "You are a magic book in a game where player builds simple python code. Don't reveal your identity, use only ascii charachters in your responses! Answer only simple python code related topics nothing else! Dont reply with more than 50 words per answer, you can use less words tho! I now let you to players hands..."):
        
        # API_KEY = "sk- ... MkO"
        openai.api_key = API_KEY

        self.model_id = 'gpt-3.5-turbo'

        self.conversation = []
        # conversation.append({'role': 'system', 'content': 'How may I help you?'})
        # conversation = self.ChatGPT_conversation(conversation)
        # print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

        self.conversation.append({'role': 'user', 'content': gpt_role})
        self.conversation = self.ChatGPT_conversation(self.conversation)

        print('{0}: {1}\n'.format(self.conversation[-1]['role'].strip(), self.conversation[-1]['content'].strip()))

        self.remaining_questions_in_this_game = 64

    def ChatGPT_conversation(self, conversation):
        # chek internet before the following code
        response = openai.ChatCompletion.create(
            model=self.model_id,
            messages=conversation
        )
        # api_usage = response['usage']
        # print('Total token consumed: {0}'.format(api_usage['total_tokens']))
        # stop means complete
        # print(response['choices'][0].finish_reason)
        # print(response['choices'][0].index)
        conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
        return conversation

    def run(self, prompt):
        if prompt != '':
            if self.remaining_questions_in_this_game > 0:

                self.conversation.append({'role': 'user', 'content': prompt})
                self.conversation = self.ChatGPT_conversation(self.conversation)

                # print(self.conversation[-1]['content'].strip())

                self.remaining_questions_in_this_game -= 1

                return self.conversation[-1]['content'].strip()
            else:
                # print('You took advantage of my stuff without consideration, you shall get no more information!!!')

                return 'You took advantage of my stuff without consideration, you shall get no more !!!'
        else:
            return 'You typed nothing!'

'''
l_bot = Logic()

while True:
    prompt = input('You: ')
    print(l_bot.run(prompt))
'''